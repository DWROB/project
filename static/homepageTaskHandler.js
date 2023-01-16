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
          doneTask(taskCard.id);
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

  const doneTask = (id) => {
    fetch("/task_handler", {
      method: "PUT",
      headers: new Headers({
        "Content-Type":"application/json"
      }),
      cache: "no-cache",
      body: JSON.stringify({ "task_id": id })
    })
    .then((response) => {
      if (response.status != 200) {
        console.log(`Request status is ${response.status}`);
        console.log(response)
        return;
      }
      response.json().then((data) => { console.log(data, response.status) })
    })
  }

  const deleteTask = (id) => {
    // console.log(`${window.origin}/task_handler`);
    fetch("/task_handler", {
      method: "DELETE",
      headers: new Headers({
        "Content-Type":"application/json"
      }),
      cache: "no-cache",
      body: JSON.stringify({ "task_id": id })
    })
    .then((response) => {
      if (response.status != 200) {
        console.log(`Request status is ${response.status}`);
        return;
      }
      response.json().then((data) => { console.log(data, response.data) });
    })
  }
});
