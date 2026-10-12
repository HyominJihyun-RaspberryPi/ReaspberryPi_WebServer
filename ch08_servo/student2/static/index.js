const angleInput = document.getElementById("angleInput");
const message = document.getElementById("message");

// 1. await를 사용하기 위해 콜백 함수 앞에 async 추가
document.getElementById("sendBtn").addEventListener("click", async function () {
    const angle = angleInput.value;
    if (angle === "" || Number(angle) < 0 || Number(angle) > 180) {
        alert("잘못된 값을 입력함");
        return;
    }

    const response = await fetch("/api/angle", {
        method: "POST",
        headers: { "Content-Type": "application/json" }, // 본문이 JSON 이라고 알려줌
        body: JSON.stringify({ angle: angle })            // {angle: 90} 을 JSON 글자로 바꿔서 담음
    });
    
    const result = await response.json();                 // 성공이든 실패든 서버는 JSON 을 보냄

    // ✏️ 1. response.ok 가 아니면 서버가 보낸 이유(result.message)를 alert 로 보여주고 멈춤
    if (!response.ok) {
        alert(result.message);
        return;
    }

    // ✏️ 2. 성공이면 result.message 를 message 에 보여줌
    message.textContent = result.message;
});
