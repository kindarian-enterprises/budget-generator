const saveBudgetbutton = document.getElementById("save-budget-button");

const budgetData = Array.from(document.querySelectorAll(".displayLabel"));

const infoOrder = {
  0: "savingsGoal",
  1: "toSave",
  2: "spendingMoney",
  3: "months",
};

async function putToDatabase(url, data) {
  const response = await fetch(url, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    body: JSON.stringify(data),
  });
  return response;
}

saveBudgetbutton.addEventListener("click", (e) => {
  const requestData = {};
  budgetData.forEach((budget, i) => {
    const itemName = infoOrder[i];
    requestData[itemName] = budget.innerHTML.match(/(\d+)/)[0];
  });
  putToDatabase("/budget", requestData)
    .then((response) => {
      if (response.status === 200) {
        window.location.href = `http://localhost/saved-budgets`;
      } else {
        throw new Error("connection failed");
      }
    })
    .catch((err) => {
      console.error(err);
    });
});
