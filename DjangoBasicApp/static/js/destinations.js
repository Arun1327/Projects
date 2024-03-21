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