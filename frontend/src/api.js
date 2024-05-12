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
        console.log(path);
        console.log(new URL(path, "http://localhost:8000/api/"));
        return new URL(path, "http://localhost:8000/api/");
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

    static createDoctor(name, email, specialty) {
        return this.makeJSONRequest("doctors/", "POST", {
            name: name,
            email: email,
            specialty: specialty,
        });

    }

    static getDoctors() {
        return this.makeJSONRequest("doctors/", "GET");

    }

    static getDoctorsByID(id) {
        return this.makeJSONRequest(`doctors/${id}`, "GET");

    }

    static createAppointment(patient_id, doctor_id, date, value) {
        return this.makeJSONRequest("appointments/", "POST", {
            patient_id: patient_id,
            doctor_id: doctor_id,
            date: date,
            value: value,
        });

    }
    static getAppointments() {
        return this.makeJSONRequest("appointments/", "GET");

    }

    static getAppointmentByID(id) {
        return this.makeJSONRequest(`appointments/${id}`, "GET");

    }

    static createPayment(appointment_id, patient_id, value) {
        return this.makeJSONRequest("payments/", "POST", {
            appointment_id: appointment_id,
            patient_id: patient_id,
            value: value,
        });

    }

    static getPayments() {
        return this.makeJSONRequest("payments/", "GET");

    }

    static getPaymentByID(id) {
        return this.makeJSONRequest(`payments/${id}`, "GET");

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


    static getAllDoctors() {
        return this.makeJSONRequest(`doctors/`);
    }
    static getDoctor(doctor_id) {
        return this.makeJSONRequest(`doctors/${doctor_id}/`);
    }
}

export default API;
