const BASE_URL = "https://codigo-g25-backend.onrender.com/api/v1/";

export async function makePost(url, body) {
  return await fetch(`${BASE_URL}${url}`, {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify(body),
  });
}

export async function verifyEmail(token) {
  return await makePost("auth/verify-email/", { token });
}

export async function singUp(inputs) {
  return await makePost("users/", inputs);
}

export async function signIn(inputs) {
  return await makePost("token", {
    username: inputs.username,
    password: inputs.password,
  });
}
