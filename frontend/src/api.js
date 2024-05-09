import config from "config.js";

// const config = { apiUrl: "https://api.moelasware.xyz/" };

const ACCEPT_JSON = {
    "Accept": "application/json",
    "Content-Type": "application/json",
};

class API {
    static getBearerToken() {
        return sessionStorage.access === undefined ? {} : {
            "Authorization": "Bearer " + sessionStorage.access,
        }
    }

    static makePathURL(path) {
        return new URL(path, config.apiUrl);
    }

    static makeRequest(
        path,
        method = "GET",
        body = undefined,
        params = undefined,
        headers = undefined
    ) {
        const searchParams = new URLSearchParams(params);
        const pathURL = this.makePathURL(path);
        searchParams.forEach((value, key) =>
            pathURL.searchParams.set(key, value)
        );

        return fetch(pathURL, {
            method: method,
            headers: { ...ACCEPT_JSON, ...headers, ...API.getBearerToken() },
            body: method === "GET" ? undefined : JSON.stringify(body),
        });
    }

    static makeJSONRequest(
        path,
        method = "GET",
        body = undefined,
        params = undefined,
        headers = undefined
    ) {
        return this.makeRequest(path, method, body, params, headers).then(
            (response) => response.json()
        );
    }


    static getUserSubmissions(user_id) {
        return this.makeJSONRequest(
            "users/" + user_id.toString() + "/submissions/"
        );
    }

    static register(username, password, repeat_password, email) {
        if (password === repeat_password) {
            return this.makeJSONRequest("register/", "POST", {
                username: username,
                password: password,
                email: email,
            });
        }
    }

    // Get user login token
    static login(username, password) {
        let tokens = this.makeJSONRequest("token/", "POST", {
            username: username,
            password: password,
        });

        tokens.then((data) => {
            sessionStorage.setItem("access", data.access);
            sessionStorage.setItem("refresh", data.refresh);
        });
        return tokens;
    }

    // Refresh token
    static tokenRefresh(refresh) {
        return this.makeJSONRequest("token/refresh/", "POST", {
            refresh: refresh,
        });
    }

    static logout() {
        return this.makeJSONRequest("token/blacklist/", "POST", {
            refresh: sessionStorage.getItem("refresh"),
        }).then(() => {
            sessionStorage.removeItem("access");
            sessionStorage.removeItem("refresh");
        });
    }

    // Post a quiz

    // Add new submission
    static createAppointment(test_id, subCorrectFormat) {
        return this.makeJSONRequest(`appointments/`, "POST", {
            answers: subCorrectFormat,
            patient: patient,
            doctor: doctor,
            specialty: specialty,
            date: date,
            is_confirmed: false,
            is_done: false,
        });
    }

    // Get user with a given id
    static getUser(user_id) {
        return this.makeJSONRequest(`users/${user_id}/`);
    }

    static getAppointments(user_id) {
        return this.makeJSONRequest(`appointments/${user_id}/`);
    }

    static getAllDoctors() {
        return this.makeJSONRequest(`doctors/`);
    }
    static getDoctor(doctor_id) {
        return this.makeJSONRequest(`doctors/${doctor_id}/`);
    }

}

export default API;
