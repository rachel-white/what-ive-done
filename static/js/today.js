//var date = new Date();
//var timestamp = date.getTime();
//function getTime() {
  //  document.getElementsByClassName("time").innerHTML = "Is the button connecting to this function";
//}


//$(document).ready(function() { 
  //          $(".time").click(function getTime(event) { 
    //            $(".time").text(event.timeStamp); 
      //      }); 
        //}); 

//$(document).ready(function() { 
  //          $(".click-for-time").click(function(event) { 
    //            $("span").text(event.timeStamp); 
      //      }); 
        //}); 

$(document).ready(function() { 
          $(".click-for-time").click(function(event) {
              var timestamp = new Date(event.timeStamp);
              var date = timestamp.toDateString()
              var time = timestamp.toTimeString()
             $(".time-add-to-db").text(timestamp + "date: " + date + " " + "time: " + time);
              document.getElementById('time').value=(time + "this is the adding to value section");
         }); 
      }); 