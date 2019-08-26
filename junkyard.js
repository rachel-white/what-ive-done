

//getTime function mostly based off this code: https://www.w3schools.com/js/tryit.asp?filename=tryjs_timing_clock but with renaming for clarity and preference. 
function getTime() {
    
    var time = "here is the time checking the displaying works"
    
    function addZero(i) {
        if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
        return i;
        }

    var date = new Date();
    var hours = date.getHours();
    var mins = date.getMinutes();
    var now = date + "" + hours + ":" + mins;
  
    hours = addZero(hours);
    mins = addZero(mins);
    
    document.getElementsByClassName("time").innerHTML = time;
}