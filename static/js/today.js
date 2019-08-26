$(document).ready(function() { 
          $(".click-for-time").click(function(event) {
              var timestamp = new Date(event.timeStamp);
              var date = timestamp.toDateString()
              var time = timestamp.toTimeString()
             $(".time-add-to-db").text(timestamp + "date: " + date + " " + "time: " + time);
              document.getElementById('time').value=(time + "time var");
              document.getElementById('date').value=(date + "date var");
         }); 
      }); 