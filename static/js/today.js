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
              var date = new Date(event.timeStamp);
              var time = date.getTime()
             $(".time-add-to-db").text(event.timeStamp + date + "time:" + time); 
              document.getElementById('time').value= (time + "this is the adding to value section");
         }); 
      }); 