const menu = document.querySelector("nav");

const hamburger = document.getElementById("burger").addEventListener("click", () => {
  menu.classList.toggle("block");
});

const modal = document.querySelector(".modal");

window.onload = () => {
  document.querySelector(".modal").innerHTML = `
    <div class="modal">
      <span class="modal-close">x</span>
      <h2 class="modal-title">Welcome to Cryptotracker<h2>
      <p class="modal-copy">On this site you can see live market updates. Comming soon are push notification on coins you want to keep track of your cryptocurrency</p>
    </div>
`;
  setTimeout(() => {
    document.querySelector(".modal").remove();
  }, 2000);

  document.querySelector(".modal-close").addEventListener('click', () => {
    modal.remove();
  });
};

fetch("https://api.coinmarketcap.com/v2/ticker/?start=0&limit=200").
then(response => {
  return response.json();
}).
then(resp => {
  console.log(resp);
  const oData = Object.getOwnPropertyNames(resp.data).slice(0, 12).map(function (i) {
    return resp.data[i];
  });
  showPrice(oData);
}).catch(err => console.log('err:' + err));

function showPrice(cryptoPrice) {

  const divs = cryptoPrice.map(function (price) {
    return `<div class="col-4">
       <div class="card">
         <h1>${price.name}</h1>
         <span><b>Symbol:</b> ${price.symbol}</span>
         <p><b>Price:</b> <span class="dollar-amount">${price.quotes.USD.price}</span></p>
         <p class="change">Change (24hr) ${price.quotes.USD.percent_change_24h}%</p>
       </div>
     </div>`;
  }).
  join("");
  document.querySelector(".results").innerHTML = `
    <div class="container max-lg text-center">${divs}</div>`;
}


fetch("https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey=2b580165d6d44c26ba2f84b75e3e9f87").
then(response => {return response.json();}).
then(resp => {
  console.log(resp);
  let articleArray = resp.articles;
  console.log(articleArray);

  showArticles(articleArray);
});

function showArticles(articleArray) {
  document.querySelector(".articles").innerHTML = `
  <div class="container padding-a-xsm">
    <div class="col-6">
      <div class="article-card">
        <img src="${articleArray[0].urlToImage}">
      <div class="article-card-body">
        <h2>${articleArray[0].title}</h2>
        <p class="margin-bottom-md">${articleArray[0].description}</p>
        <a class="read-more-btn" href="${articleArray[0].url}" target="_blank">Read More</a>
       </div>
      </div>
    </div>
    <div class="col-6">
      <div class="article-card">
        <img src="${articleArray[1].urlToImage}">
        <div class="article-card-body">
          <h2>${articleArray[1].title}</h2>
          <p class="margin-bottom-md">${articleArray[1].description}</p>
          <a class="read-more-btn" href="${articleArray[1].url}" target="_blank">Read More</a>
        </div>
      </div>
    </div>
    <div class="col-6">
      <div class="artcile-card">
        <img src="${articleArray[2].urlToImage}">
        <div class="article-card-body">
          <h2>${articleArray[2].title}</h2>
          <p class="margin-bottom-md">${articleArray[2].description}</p>
          <a class="read-more-btn" href="${articleArray[2].url}" target="_blank">Read More</a>
        </div>
      </div>
     </div>
     <div class="col-6">
      <div class="artcile-card">
        <img src="${articleArray[3].urlToImage}">
        <div class="article-card-body">
          <h2>${articleArray[3].title}</h2>
          <p class="margin-bottom-md">${articleArray[3].description}</p>
          <a class="read-more-btn" href="${articleArray[3].url}" target="_blank">Read More</a>
        </div>
      </div>
     </div>
  </div>
`;
}

const signUpForm = document.getElementById("sign-up-form");
const errorMsg = document.querySelector(".error-message");
signUpForm.addEventListener("submit", validateForm);

function validateForm(e) {
  e.preventDefault();
  const emailField = document.querySelector(".email-input");
  if (emailField.value === "") {
    emailField.style.border = "1px solid red";
    errorMsg.style.display = "block";
  } else {
    emailField.value = "";
    emailField.style.border = "";
    errorMsg.style.display = "none";
  }
}

const footerDate = document.querySelector(".date");
const date = new Date();
footerDate.innerHTML = `Copyright ${date.getFullYear()}`;