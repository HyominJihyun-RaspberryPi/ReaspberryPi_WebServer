let n = 0;

const num = document.getElementById("num");
const numInput = document.getElementById("numInput");
const increase = document.getElementById("increase");

increase.addEventListener("click", function () {
    n = n + 1;
    num.innerHTML = n;
    numInput.value = n;   // 폼으로 보낼 값도 같이 갱신
});

submit.addEventListener("click", function() {
    location.href='http://10.150.1.26:5001/'+n
    n = 0;
    num.innerHTML = n;
})
