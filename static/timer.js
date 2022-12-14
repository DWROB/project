// run script once DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
  timeChoice = document.querySelector("#time-select");
  startBtn = document.getElementById("start-timer");
  cancelBtn = document.getElementById("cancel-timer");
  timerVisual = document.getElementById("timer-visual");

  saveModal = document.getElementById("myModal");

  let selection;
  var intervalID;

  timeChoice.addEventListener("change", function (e) {
    selection = e.target.value;
    console.log(selection);

    // trying to get the modal up
    saveModal.setAttribute("visibility", "visible");
    //     saveModal.classList.remove('visible');

    return selection;
  });

  startBtn.addEventListener("click", function () {
    console.log("start button " + selection);
    console.log(typeof selection);

    let minutes;
    let seconds;

    switch (selection) {
      case "1":
        // 5 seconds
        minutes = 0;
        seconds = 5;
        console.log(minutes + ":" + seconds);
        intervalID = setInterval(pomoCounter, 1000);
        return minutes, seconds;
      case "2":
        // 30 minutes
        minutes = 29;
        seconds = 60;
        console.log(minutes + ":" + seconds);
        intervalID = setInterval(pomoCounter, 1000);
        return minutes, seconds;
      case "3":
        // 35 minutes
        minutes = 34;
        seconds = 60;
        console.log(minutes + ":" + seconds);
        intervalID = setInterval(pomoCounter, 1000);
        return minutes, seconds;
      case "4":
        // 40
        minutes = 39;
        seconds = 60;
        console.log(minutes + ":" + seconds);
        intervalID = setInterval(pomoCounter, 1000);
        return minutes, seconds;
      default:
        alert("Please select a pomo time!");
        break;
    }

    function pomoCounter() {
      // decrment minutes if needed
      if (minutes > 0 && seconds === 0) {
        minutes--;
        seconds = 60;
        console.log(minutes + ":" + seconds);
      }

      // decrement seconds
      seconds--;
      console.log(minutes + ":" + seconds);

      // TO DO:  put the counter on the DOM
      if (seconds < 10) {
        timerVisual.innerText = minutes + ":0" + seconds;
      } else {
        timerVisual.innerText = minutes + ":" + seconds;
      }

      if (seconds === 0 && minutes === 0) {
        clearInterval(intervalID);
        timerVisual.innerText = "00:00";
        alert("Fuckin' Finally");
      }
      return minutes, seconds;
    }
  });

  cancelBtn.addEventListener("click", function () {
    if (intervalID) {
      clearInterval(intervalID);
    }
    minutes = 0;
    seconds = 0;
    return minutes, seconds;
  });
});
