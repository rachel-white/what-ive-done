function generateTime(event) {
              var timestamp = new Date();
              var date = timestamp.toDateString();
              var hourtime = timestamp.getHours();
              var minstime = timestamp.getMinutes();
              var secondstime = timestamp.getSeconds();
              var time = (hourtime + ":" + minstime +  ":" + secondstime); 
              console.log("time: " + time)
              document.getElementById('time').value=(time);
              document.getElementById('date').value=(date);
         }; 
         
