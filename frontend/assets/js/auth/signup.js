/**
 * form 을 선택하고 직렬화된 JSON 을 반환합니다.
 */
function getFormJson() {
  let loginForm = document.querySelector(".signup-form");
  let data = new FormData(loginForm);
  let serializedFormData = serialize(data);
  return JSON.stringify(serializedFormData);
}

/**
 * form 데이터를 받아서 JSON으로 직렬화합니다.
 */
function serialize(rawFormData) {
  let result = {};
  for (let [key, value] of rawFormData) {
    let sel = document.querySelectorAll("[name=" + key + "]");
    if (sel.length > 1) {
      if (result[key] === undefined) {
        result[key] = [];
      }
      result[key].push(value);
    } else {
      result[key] = value;
    }
  }
  return result;
}

/**
 * 서버에 회원가입 요청을 보냅니다.
 */
async function submitSignupData() {
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  var requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: getFormJson(),
    redirect: "follow",
  };
  const response = await fetch(SIGNUP_API_URL, requestOptions);
  if (response.status == 201) {
    alert(JSON.stringify(await response.json()));
    window.location.href = FRONTEND_SERVER_BASE_URL + "/flastagram/login";
  } else {
    alert(JSON.stringify(await response.json()));
  }
}
