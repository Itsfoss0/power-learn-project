const mybtn = document.getElementById('button1');
const timesClicked = document.getElementById('clicked');

console.log(mybtn.innerText);
console.log(timesClicked.innerText)

let times = 0;

mybtn.addEventListener("click", () => {
    
    if (times >= 100) {
        alert('Hey, I\'m tired man, stop pocking me!, lets start again');
        times = 0;
    } else {
        timesClicked.textContent = ` Button clicked  ${times} times`;
        times += 1;
    }
});