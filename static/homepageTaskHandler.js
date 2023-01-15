document.addEventListener("DOMContentLoaded", function () {
  console.log("task handler loaded!");

  // task done - update db and turn the card green.
  tasksCards = document.querySelectorAll(".card-item");

  // task delete - remove from db and dom

  doneBtns = document.querySelectorAll("#done");
  deleteBtns = document.querySelectorAll("#delete");

  doneBtns.forEach(function (doneBtn) {
    doneBtn.addEventListener("click", async function () {
      // handle the color and button text change.
      tasksCards.forEach(function (taskCard) {
        if (taskCard.id === doneBtn.value) {
          taskCard.classList.toggle("task-done-color");
          if (doneBtn.innerText === "To Do!") {
            doneBtn.innerText = "Done";
          } else {
            doneBtn.innerText = "To Do!";
          }
          // AJAX function to patch db and change completed: true or false.
        }
      });
    });
  });

  deleteBtns.forEach(function (deleteBtn) {
    deleteBtn.addEventListener("click", async function () {
      console.log(deleteBtn.classList);
      tasksCards.forEach(function (taskCard) {
        if (taskCard.id === deleteBtn.value) {
          taskCard.remove();
          // AJAX function to remove the task from db.
          deleteTask(taskCard.id);
        }
      });
    });
  });

  const deleteTask = (id) => {
    console.log(`${window.origin}/taskHandler`);
    fetch("/taskHandler", {
      method: "POST",
      headers: new Headers({
        "Content-Type":"application/json"
      }),
      cache: "no-cache",
      body: JSON.stringify({ "request": id })
    })
    .then((response) => {
      if (response.status != 200){
        console.log(`Request status is ${response.status}`);
        return;
      }
      response.json().then((data) => { console.log(data)});
    })
  }
});
