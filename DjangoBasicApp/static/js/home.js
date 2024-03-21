

document.addEventListener('DOMContentLoaded', () => {
    const scrollable = document.getElementById('scrollable');
    let isDragging = false;
    let startX;
    let scrollLeft;
  
    scrollable.addEventListener('mousedown', (e) => {
      isDragging = true;
      startX = e.clientX - scrollable.offsetLeft;
      scrollLeft = scrollable.scrollLeft;
    });
  
    scrollable.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      e.preventDefault();
      const x = e.clientX - scrollable.offsetLeft;
      const scrollX = (x - startX) * 1.5;
      scrollable.scrollLeft = scrollLeft - scrollX;
    });
  
    scrollable.addEventListener('mouseup', () => {
      isDragging = false;
    });
  
    scrollable.addEventListener('mouseleave', () => {
      isDragging = false;
    });
  });
  

// swapping of from and to with the icon on clicked
  function swapicon(){
    var inputFrom=document.getElementById('inputFrom').value;
    var inputTo=document.getElementById('inputTo').value;
    
    document.getElementById('inputFrom').value = inputTo;
    document.getElementById('inputTo').value = inputFrom;
  }



  // Get today's date in the format "yyyy-mm-dd"
  var today = new Date().toISOString().split('T')[0];
  
  // Set the minimum date for the input field
  document.getElementById("futureDate").min = today;