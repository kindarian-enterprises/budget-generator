// const APP_URL = process.env("APPURL");

const listObject = document.querySelector(".saved_budget_list");
window.addEventListener("load", function (e) {
  console.log("Page loaded!");
  fetch("http://127.0.0.1/budget/")
    .then((response) => response.json())
    .then((data) => {
      if (data.length === 0) {
        listObject.innerHTML = `
        <ul>
        <li>Try adding your first budget to get started!</li>
        </ul>
    `;
      } else {
        data.forEach((budget) => {
          let Budget = JSON.parse(budget);
          listObject.innerHTML = `
        <ul>
        <li>Your Goal: $${Budget["goal"]}--Months Until Goal: ${Budget["timeUntilGoal"]}--Spending Money: $${Budget["monthlySpending"]}--Money to be Saved: $${Budget["monthlySaving"]}</li>
        </ul>
    `;
        });
      }
    });
});
