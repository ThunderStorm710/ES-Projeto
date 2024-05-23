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
        return new URL(path, "http://clinicaenv.eba-3k2xhunz.us-east-1.elasticbeanstalk.com/api/");
    }

    static async makeRequest(
        path,
        method = "GET",
        body = undefined,
        params = undefined,
        headers = {}
    ) {
        const searchParams = new URLSearchParams(params);
        const pathURL = this.makePathURL(path);
        searchParams.forEach((value, key) =>
            pathURL.searchParams.set(key, value)
        );

        const options = {
            method: method,
            headers: {
                ...headers,
                ...API.getBearerToken(),
            },
            body: method === "GET" ? undefined : body,
        };

        const response = await fetch(pathURL, options);
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.message || 'Something went wrong');
        }
        return response.json();
    }

    static makeJSONRequest(
        path,
        method = "GET",
        body = undefined,
        params = undefined,
        headers = {}
    ) {
        // Se o corpo for uma instância de FormData, não definimos o cabeçalho 'content-type'
        if (!(body instanceof FormData)) {
            headers['Content-Type'] = 'application/json';
            body = JSON.stringify(body);
        }

        return this.makeRequest(path, method, body, params, headers);
    }

    static searchFace(appointmentId, title, content, image) {
        const formData = new FormData();
        formData.append('appointmentId', appointmentId);
        formData.append('title', title);
        formData.append('content', content);
        if (image) {
            formData.append('image', image);
        }

        return this.makeRequest("searchFace/", "POST", formData);
    }

    static indexFace(appointmentId, title, content, image) {
        const formData = new FormData();
        formData.append('appointmentId', appointmentId);
        formData.append('title', title);
        formData.append('content', content);
        if (image) {
            formData.append('image', image);
        }

        return this.makeRequest("indexFace/", "POST", formData);
    }


    static register(username, password, repeat_password, email) {
        if (password === repeat_password) {
            return this.makeJSONRequest("registration/", "POST", {
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

    static createAppointment(patient_id, doctor_id, slot_id, value) {
        return this.makeJSONRequest("appointments/", "POST", {
            patient_id: patient_id,
            doctor_id: doctor_id,
            slot_id: slot_id,
            value: value,
        });

    }

    static getAppointments() {
        return this.makeJSONRequest("all-appointments/", "GET");

    }

    static getAppointmentByID(id) {
        return this.makeJSONRequest(`appointments/${id}`, "GET");

    }

    static getAppointmentByPatientID() {
        return this.makeJSONRequest(`user/appointments/`, "GET");

    }

    static beginAppointment(image) {
        return this.makeJSONRequest("upload/", "POST", {
            image: image,
        });

    }

    static createSpecialty(name) {
        return this.makeJSONRequest("specialty/", "POST", {
            name: name,
        });

    }

    static getSpecialty() {
        return this.makeJSONRequest("specialty/", "GET");

    }

    static createPayment(appointment_id, patient_id, value) {
        return this.makeJSONRequest("payments/", "POST", {
            appointment_id: appointment_id,
            patient_id: patient_id,
            value: value,
        });

    }

    static finishAppointment(appointment_id, patient_id) {
        return this.makeJSONRequest("appointment/finish/", "POST", {
            appointment_id: appointment_id,
            patient_id: patient_id,
        });

    }

    static getPayments() {
        return this.makeJSONRequest("all-payments/", "GET");

    }

    static getPaymentByID(id) {
        return this.makeJSONRequest(`payment/${id}`, "GET");

    }

    static getPaymentByPatientID() {
        return this.makeJSONRequest(`user/payments/`, "GET");

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

    static getDoctorsBySpecialtyId(speacialty_id) {
        return this.makeJSONRequest(`specialty/${speacialty_id}/doctors/`);
    }

    static getTimeSlotsByDoctorId(doctor_id) {
        return this.makeJSONRequest(`doctors/${doctor_id}/slots/`);
    }


    static getDateSlotsByDoctorId(doctor_id) {
        return this.makeJSONRequest(`doctors/${doctor_id}/slots/day/`);
    }
}

export default API;
