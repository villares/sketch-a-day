from ursina import *
import numpy as np

from ursina.prefabs.first_person_controller import FirstPersonController

number_of_particles = 1000   # keep this as low as possible
points = np.array([Vec3(0,0,0) for i in range(number_of_particles)])
directions = np.array([Vec3(random.random()-.5,random.random()-.5,random.random()-.5)*.05 for i in range(number_of_particles)])
frames = []

# simulate the particles once and cache the positions in a list.
for i in range(60*1):
    points += directions
    frames.append(copy(points))


class ParticleSystem(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=Mesh(vertices=points, mode='point', static=False, render_points_in_3d=True, thickness=.1), t=0, duration=1, **kwargs)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def update(self):
        self.t += time.dt
        if self.t >= self.duration:
            destroy(self)
            return

        self.model.vertices = frames[floor(self.t * 60)]
        self.model.generate()



if __name__ == '__main__':
    app = Ursina(vsync=False)
    window.color = color.black
    player = FirstPersonController(model='cube', z=-10, color=color.orange, origin_y=-.5, speed=8, collider='box')


    def input(key):
        if key == 'space':
            p = ParticleSystem(position=Vec3(random.random(),random.random(),random.random())*2, color=color.random_color(), rotation_y=random.random()*360)
            p.fade_out(duration=100, delay=100-.2, curve=curve.linear)
        elif key == 'q':
            exit()

    Text('press space to spawn particles', origin=(0,0), y=-.45)
    EditorCamera()

    app.run()



# from ursina import *
# from ursina.prefabs.first_person_controller import FirstPersonController
# from ursina.shaders import lit_with_shadows_shader
# 
# app = Ursina()
# 
# random.seed(0)
# Entity.default_shader = lit_with_shadows_shader
# 
# ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
# 
# editor_camera = EditorCamera(enabled=False, ignore_paused=True)
# player = FirstPersonController(model='cube', z=-10, color=color.orange, origin_y=-.5, speed=8, collider='box')
# player.collider = BoxCollider(player, Vec3(0,1,0), Vec3(1,2,1))
# 
# gun = Entity(model='cube', parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1), origin_z=-.5, color=color.red, on_cooldown=False)
# gun.muzzle_flash = Entity(parent=gun, z=1, world_scale=.5, model='quad', color=color.yellow, enabled=False)
# 
# shootables_parent = Entity()
# mouse.traverse_target = shootables_parent
# 
# 
# for i in range(16):
#     Entity(model='cube', origin_y=-.5, scale=2, texture='brick', texture_scale=(1,2),
#         x=random.uniform(-8,8),
#         z=random.uniform(-8,8) + 8,
#         collider='box',
#         scale_y = random.uniform(2,3),
#         color=color.hsv(0, 0, random.uniform(.9, 1))
#         )
# 
# def update():
#     if held_keys['left mouse']:
#         shoot()
# 
# def shoot():
#     if not gun.on_cooldown:
#         # print('shoot')
#         gun.on_cooldown = True
#         gun.muzzle_flash.enabled=True
#         from ursina.prefabs.ursfx import ursfx
#         ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)], volume=0.5, wave='noise', pitch=random.uniform(-13,-12), pitch_change=-12, speed=3.0)
#         invoke(gun.muzzle_flash.disable, delay=.05)
#         invoke(setattr, gun, 'on_cooldown', False, delay=.15)
#         if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
#             mouse.hovered_entity.blink(color.red)
#             mouse.hovered_entity.hp -= 10
# 
# 
# from ursina.prefabs.health_bar import HealthBar
# 
# class Enemy(Entity):
#     def __init__(self, **kwargs):
#         super().__init__(parent=shootables_parent, model='cube', scale_y=2, origin_y=-.5, color=color.light_gray, collider='box', **kwargs)
#         self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
#         self.max_hp = 100
#         self.hp = self.max_hp
# 
#     def update(self):
#         dist = distance_xz(player.position, self.position)
#         if dist > 40:
#             return
# 
#         self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)
# 
# 
#         self.look_at_2d(player.position, 'y')
#         hit_info = raycast(self.world_position + Vec3(0,1,0), self.forward, 30, ignore=(self,))
#         # print(hit_info.entity)
#         if hit_info.entity == player:
#             if dist > 2:
#                 self.position += self.forward * time.dt * 5
# 
#     @property
#     def hp(self):
#         return self._hp
# 
#     @hp.setter
#     def hp(self, value):
#         self._hp = value
#         if value <= 0:
#             destroy(self)
#             return
# 
#         self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
#         self.health_bar.alpha = 1
# 
# # Enemy()
# enemies = [Enemy(x=x*4) for x in range(4)]
# 
# 
# def pause_input(key):
#     if key == 'tab':    # press tab to toggle edit/play mode
#         editor_camera.enabled = not editor_camera.enabled
# 
#         player.visible_self = editor_camera.enabled
#         player.cursor.enabled = not editor_camera.enabled
#         gun.enabled = not editor_camera.enabled
#         mouse.locked = not editor_camera.enabled
#         editor_camera.position = player.position
# 
#         application.paused = editor_camera.enabled
# 
# pause_handler = Entity(ignore_paused=True, input=pause_input)
# 
# 
# sun = DirectionalLight()
# sun.look_at(Vec3(1,-1,-1))
# Sky()
# 
# app.run()
# 
# 