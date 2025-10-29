# https://github.com/py5coding/python-brasil-2025/blob/main/prototypes/facets.py

import numpy as np
import py5
import trimesh
from trimesh.util import pairwise


def get_boundaries(shape, min_angle=0.0):
    boundaries = []

    # first, get the boundaries of the facets
    for facet_boundary in shape.facets_boundary:
        # each facet_boundary is an (n, 2) array of vertex indices
        facet_boundary_edges = {tuple(edge) for edge in facet_boundary.tolist()}

        while facet_boundary_edges:
            # start a new boundary chain
            edge = facet_boundary_edges.pop()
            boundary = [edge[0], edge[1]]

            while boundary[0] != boundary[-1]:
                # find the next edge to continue the boundary chain, stopping
                # if a loop is formed or no connecting edge is found
                for next_edge in facet_boundary_edges:
                    if next_edge[0] == boundary[-1]:
                        boundary.append(next_edge[1])
                        facet_boundary_edges.remove(next_edge)
                        # found it
                        break
                    elif next_edge[1] == boundary[-1]:
                        boundary.append(next_edge[0])
                        facet_boundary_edges.remove(next_edge)
                        # found it
                        break
                else:
                    # didn't find a connecting edge, move on to the next facet
                    break

            # note that boundary[0] == boundary[-1], forming a closed loop
            boundaries.append(boundary)

    # faces with no adjacent and coplanar faces are not part of any facet
    # need to identify the non-facet faces and add their edges as boundaries

    # first, find all faces that are part of facets
    facet_faces = set()
    for facet in shape.facets:
        facet_faces.update(facet.tolist())

    # subtract from the set of all faces to get the non-facet faces
    all_faces = set(np.arange(len(shape.faces)).tolist())
    non_facet_faces = all_faces - facet_faces

    # now add the edges of the non-facet faces as boundaries
    for face in shape.faces[list(non_facet_faces)].tolist():
        # the face + [face[0]] bit is so that boundary[0] == boundary[-1]
        boundaries.append(face + [face[0]])

    # now filter the boundaries to remove edges with angles below min_angle
    exclude_edges = set()
    for edge in shape.face_adjacency_edges[shape.face_adjacency_angles < min_angle]:
        exclude_edges.add((int(edge[0]), int(edge[1])))
        exclude_edges.add((int(edge[1]), int(edge[0])))

    filtered_boundaries = []
    for boundary in boundaries:
        filtered_boundary = []
        boundary_segment = []

        for a, b in pairwise(boundary):
            if (a, b) in exclude_edges:
                if boundary_segment:
                    # save segment and start a new one
                    filtered_boundary.append(boundary_segment)
                    boundary_segment = []
            else:
                if not boundary_segment:
                    # starting a new segment, add the starting vertex
                    boundary_segment.append(a)
                boundary_segment.append(b)

        if boundary_segment:
            # save any remaining segment
            filtered_boundary.append(boundary_segment)

        if len(filtered_boundary) == 1:
            # if there's only one, none of the edges were filtered out
            filtered_boundaries.append(filtered_boundary[0])
        elif filtered_boundary:
            # len(filtered_boundary) >= 2, need to see if the first and last
            # can be connected
            if filtered_boundary[0][0] == filtered_boundary[-1][-1]:
                # connect first and last segments to make one continuous segment
                merged_segment = filtered_boundary[-1][:-1] + filtered_boundary[0]
                filtered_boundaries.append(merged_segment)
                filtered_boundaries.extend(filtered_boundary[1:-1])
            else:
                filtered_boundaries.extend(filtered_boundary)

    return filtered_boundaries


def trimesh_facet_conversion(
    sketch: py5.Sketch, shape: trimesh.Trimesh, **kwargs
) -> py5.Py5Shape:
    boundaries = get_boundaries(shape, min_angle=kwargs.get("min_angle", 0.0))

    facet_shape = sketch.create_shape(sketch.GROUP)

    # first, the base shape with all the triangles and no lines
    base_shape = sketch.create_shape()
    with base_shape.begin_shape(sketch.TRIANGLES):
        base_shape.no_stroke()
        base_shape.vertices(shape.vertices[shape.faces.flatten()])
    facet_shape.add_child(base_shape)

    # now add the boundary lines
    for boundary in boundaries:
        # each boundary will be its own child shape
        boundary_shape = sketch.create_shape()

        if boundary[0] == boundary[-1]:
            # indicates a closed loop / closed shape
            with boundary_shape.begin_closed_shape():
                boundary_shape.no_fill()
                boundary_shape.vertices(shape.vertices[boundary])
        else:
            if len(boundary) == 2:
                # two vertices means no tesselation, need to draw a line
                # see https://github.com/py5coding/py5generator/issues/659
                with boundary_shape.begin_shape(py5.LINES):
                    boundary_shape.vertices(shape.vertices[boundary])
            else:
                # open shape with more than three or more vertices
                with boundary_shape.begin_shape():
                    boundary_shape.no_fill()
                    boundary_shape.vertices(shape.vertices[boundary])

        facet_shape.add_child(boundary_shape)

    return facet_shape


def trimesh_facet_conversion_precondition(shape):
    return isinstance(shape, trimesh.Trimesh)


py5.register_shape_conversion(
    trimesh_facet_conversion_precondition, trimesh_facet_conversion
)