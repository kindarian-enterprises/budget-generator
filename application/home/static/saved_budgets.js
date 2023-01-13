// const APP_URL = process.env("APPURL");

const listObject = document.getElementById("saved_budget_list");
window.addEventListener("load", function (e) {
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
        const uListEl = document.createElement("ul");
        data.forEach((budget, i, arr) => {
          const Budget = JSON.parse(budget);
          const budgetDate = new Date();
          budgetDate.setTime(Budget.dateCreated.$date);

          const listEl = this.document.createElement("li");

          const textNode1 = document.createTextNode(checkNumLength(Budget));
          const textNode2 = this.document.createTextNode(
            `Date Created: ${budgetDate.toLocaleDateString()}`
          );

          listEl.classList.add(
            `budget-list-${i === arr.length - 1 ? "element-last" : "element"}`
          );
          listEl.appendChild(textNode1);
          listEl.appendChild(textNode2);
          uListEl.appendChild(listEl);
          listObject.appendChild(uListEl);
        });
      }
    });
});

function checkNumLength(value) {
  let numLength = value["goal"].toString().length;
  // console.log(typeof value["goal"]);
  if (numLength >= 11) {
    return `Your Goal: $${value["goal"]}`;
  } else {
    const spaceVal = 11 - numLength;
    // console.log(spaceVal, numLength);
    return `Your Goal: $${value["goal"]}${"\xa0\xa0".repeat(spaceVal)}`;
  }
}
