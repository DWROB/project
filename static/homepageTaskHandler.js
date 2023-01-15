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
        }
      });
    });
  });
});
