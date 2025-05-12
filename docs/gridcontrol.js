<!-- Layout controls --
    <div class="layout-controls" style="display: none;">
      <button id="toggleLayout">grid layout</button>
      <div id="gridControls" style="display: none;">
        <label for="columnWidth">column width (px):</label>
        <input type="number" id="columnWidth" min="150" max="400" value="200">
      </div>
    </div>
 -->


<!-- Script to handle the layout toggling -->

  document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const yearsHr = document.querySelector('hr.years');
    const controlsDiv = document.querySelector('.layout-controls');
    const toggleButton = document.getElementById('toggleLayout');
    const gridControls = document.getElementById('gridControls');
    const columnWidthInput = document.getElementById('columnWidth');
    const sketchesContainer = document.querySelector('.content .sketches');
    
    // Show the controls and insert after years HR
    if (yearsHr && controlsDiv) {
      controlsDiv.style.display = 'flex';
      // Insert controls after the years HR
      yearsHr.parentNode.insertBefore(controlsDiv, yearsHr.nextSibling);
    }
    
    // Initialize
    let isGridLayout = false;
    let sketchItems = [];
    
    // Create virtual sketch items by finding all H3 sections
    function createVirtualSketchItems() {
      sketchItems = [];
      const h3Elements = sketchesContainer.querySelectorAll('h3');
      
      h3Elements.forEach((h3, index) => {
        // Create a sketch item object
        const sketchItem = {
          h3: h3,
          elements: [h3],
          startIndex: Array.from(sketchesContainer.children).indexOf(h3),
          endIndex: null
        };
        
        // Find all elements between this h3 and the next h3 or HR
        let currentElement = h3.nextElementSibling;
        while (currentElement && currentElement.tagName !== 'H3' && 
              (currentElement.tagName !== 'HR' || 
               (currentElement.tagName === 'HR' && !currentElement.nextElementSibling?.tagName === 'H3'))) {
          sketchItem.elements.push(currentElement);
          currentElement = currentElement.nextElementSibling;
        }
        
        // Set the end index
        sketchItem.endIndex = sketchItem.startIndex + sketchItem.elements.length - 1;
        sketchItems.push(sketchItem);
      });
      
      return sketchItems;
    }
    
    // Apply grid layout
    function applyGridLayout() {
      // Get current settings
      const columnWidth = columnWidthInput.value + 'px';
      
      // Apply grid styles to sketches container
      sketchesContainer.classList.add('multi-column');
      sketchesContainer.style.gridTemplateColumns = `repeat(auto-fill, minmax(${columnWidth}, 1fr))`;
      sketchesContainer.style.gridGap = '20px';
      
      // Create virtual sketch items if needed
      if (sketchItems.length === 0) {
        createVirtualSketchItems();
      }
      
      // Wrap each sketch item's elements with a div
      sketchItems.forEach((item, index) => {
        // Check if this item is already wrapped
        if (!item.wrapper) {
          // Create a wrapper div
          const wrapper = document.createElement('div');
          wrapper.classList.add('sketch-item');
          wrapper.id = `sketch-item-${index}`;
          
          // Insert the wrapper before the first element
          item.h3.parentNode.insertBefore(wrapper, item.h3);
          
          // Move all elements to the wrapper
          item.elements.forEach(el => {
            wrapper.appendChild(el);
          });
          
          // Store the wrapper reference
          item.wrapper = wrapper;
        }
      });
    }
    
    // Remove grid layout and restore original structure
    function removeGridLayout() {
      sketchesContainer.classList.remove('multi-column');
      sketchesContainer.style.gridTemplateColumns = '';
      sketchesContainer.style.gridGap = '';
      
      // Unwrap all sketch items
      sketchItems.forEach(item => {
        if (item.wrapper) {
          const parent = item.wrapper.parentNode;
          
          // Move all elements back to the original container
          while (item.wrapper.firstChild) {
            parent.insertBefore(item.wrapper.firstChild, item.wrapper);
          }
          
          // Remove the empty wrapper
          parent.removeChild(item.wrapper);
          item.wrapper = null;
        }
      });
    }
    
    // Toggle between layouts
    toggleButton.addEventListener('click', function() {
      isGridLayout = !isGridLayout;
      
      if (isGridLayout) {
        applyGridLayout();
        gridControls.style.display = 'inline-flex';
        toggleButton.textContent = 'Single Column';
      } else {
        removeGridLayout();
        gridControls.style.display = 'none';
        toggleButton.textContent = 'Grid Layout';
      }
    });
    
    // Update grid layout when column width changes
    columnWidthInput.addEventListener('input', function() {
      if (isGridLayout) {
        sketchesContainer.style.gridTemplateColumns = `repeat(auto-fill, minmax(${this.value}px, 1fr))`;
      }
    });
  });