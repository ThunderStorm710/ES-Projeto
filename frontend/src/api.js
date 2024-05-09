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

    // Get test by ID
    static getTest(test_id) {
        return this.makeJSONRequest(`tests/${test_id}/`);
    }

    // Get all submissions of a test
    static getTestSubmissions(test_id) {
        return this.makeJSONRequest(`tests/${test_id}/submissions/`);
    }

    // Get all tests
    static getTests() {
        return this.makeJSONRequest("tests/");
    }

    static canCreateTest() {
        return this.makeJSONRequest(`user/can_create/test/`);
    }

    // Get all tests including My submissions
    static getTestsMySub() {
        return this.makeJSONRequest(
            "tests/?" +
                new URLSearchParams({
                    includeMySubmissions: true,
                })
        );
    }

    // Get a tag by ID
    static getTag(tag_id) {
        return this.makeJSONRequest(`tags/${tag_id}/`);
    }

    // Get all tags
    static getTags() {
        return this.makeJSONRequest("tags/");
    }

    // Get num_quizzes quizzes with tags in tags list (no tags ==> any tags allowed)
    static genQuizzes(num_quizzes, tags) {
        return this.makeJSONRequest("quizzes/gen/", "POST", {
            num_quizzes: num_quizzes,
            tags: tags,
        });
    }

    // Get all possible answers for a given quiz
    static getQuizAnswers(quiz_id) {
        return this.makeJSONRequest(`quizzes/${quiz_id}/answers/`);
    }

    // Get number of quizzes in db
    static getNumQuizzes() {
        return this.makeJSONRequest("quizzes/count/");
    }

    // Get a quiz by ID
    static getQuiz(quiz_id) {
        return this.makeJSONRequest(`quizz/${quiz_id}/`);
    }

    // NOT YET IMPLEMENTED
    // Get all quizzes
    static getQuizzes() {
        return this.makeJSONRequest("quizzes/");
    }

    // Get all reviewers of a given quiz
    static getQuizReviewers(quiz_id) {
        return this.makeJSONRequest(`quizzes/${quiz_id}/reviewers/`);
    }

    // NOT WORKING IN BACKEND
    // Create a quiz review
    static createQuizReview(quiz, reviewer, accepted, comment) {
        return this.makeJSONRequest("quizzes/review/", "POST", {
            quiz: quiz,
            reviewer: reviewer,
            accepted: accepted,
            comment: comment,
        });
    }

    static createQuiz(inputs, flag) {
        return this.makeJSONRequest("quizzes/", "POST", {
            inputs: inputs,
            flag: flag,
        });
    }
    static editQuiz(inputs, id, flag) {
        return this.makeJSONRequest(`quizzes/${id}/`, "PATCH", {
            inputs: inputs,
            flag: flag,
        });
    }

    static getvalid() {
        return this.makeJSONRequest("review/validate/");
    }

    static getQuizzesOfReviewer() {
        return this.makeJSONRequest("review/quizzes/");
    }

    static getQuizInfoReview(pk) {
        return this.makeJSONRequest(`review/quizzes/${pk}/`);
    }

    // Get all test submissions made by a given user
    static getUserSubmissions(user_id) {
        return this.makeJSONRequest(
            "users/" + user_id.toString() + "/submissions/"
        );
    }

    // Get hall of fame
    static getHallOfFameTests() {
        return this.makeJSONRequest("fame/tests/");
    }

    // Get hall of fame users
    static getHallOfFameUsers() {
        return this.makeJSONRequest("fame/users/");
    }

    // Get hall of fame test by Id
    static getHallOfFameTestById(id) {
        return this.makeJSONRequest(
            "fame/tests/" + id.toString() + "/submissions/"
        );
    }

    // Get hall of fame user by Id
    static getHallOfFameUserById(id) {
        return this.makeJSONRequest(
            "fame/users/" + id.toString() + "/submissions/"
        );
    }

    static getMyFinishedQuizzes() {
        return this.makeJSONRequest("myquizzes/");
    }

    static getInfoQuiz(id) {
        return this.makeJSONRequest(`quiz/${id}/info/`);
    }

    static getReviewsOfQuiz(id) {
        return this.makeJSONRequest(`quiz/${id}/reviews/`);
    }

    static createReview(args) {
        return this.makeJSONRequest("review/create/", "POST", {
            args: args,
        });
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

    // TODO: implement register

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

    // THE FOLLOWING ENDPOINTS ARE NOT IMPLEMENTED IN BACKEND

    // Add revision
    static addRevision(quiz_id) {
        return this.makeJSONRequest(`quizzes/${quiz_id}/`, "PATCH");
    }

    // Post a quiz
    static postQuiz(question, accepted, answers) {
        return this.makeJSONRequest("quizzes/", "POST", {
            question: question,
            accepted: accepted,
            answers: answers,
        });
    }

    // Get profile
    static getProfile() {
        return this.makeJSONRequest("profile/");
    }

    // Get rejected reviews
    static getRejectedReviews(quiz_id) {
        return this.makeJSONRequest(`quizzes/${quiz_id}/revisions/`);
    }

    static getInfoReview(pk) {
        return this.makeJSONRequest("review/quiz/" + pk.toString() + "/");
    }

    // Get a quizz's reviews
    static getQuizzReview(quiz_id) {
        return this.makeJSONRequest(`quizzes/${quiz_id}/reviews/`);
    }

    // Post a review
    static postQuizzReview(quiz_id) {
        return this.makeJSONRequest(`quizzes/${quiz_id}/reviews/`, "POST");
    }

    // Generate a new test
    static postTest(name, author, quiz_ids) {
        return this.makeJSONRequest("tests/", "POST", {
            name: name,
            // TODO: author needs to be removed from payload, it should be derived from request
            // authentication   ~tomasduarte
            author: author,
            quizzes: quiz_ids,
        });
    }

    // Get all submissions of a given test
    static getAllTestSubmissions(test_id) {
        return this.makeJSONRequest(`tests/${test_id}/submissions/`);
    }

    // Add new submission
    static postSubmission(test_id, subCorrectFormat) {
        return this.makeJSONRequest(`tests/${test_id}/submissions/`, "POST", {
            answers: subCorrectFormat,
        });
    }

    // Get user with a given id
    static getUser(user_id) {
        return this.makeJSONRequest(`users/${user_id}/`);
    }

    static getDrafts() {
        return this.makeJSONRequest("drafts/");
    }

    static getDraftById(quiz_id) {
        return this.makeJSONRequest(`draft/${quiz_id}/`);
    }

    static getXML() {
        return this.makeRequest("quiz/export/").then((res) => { return res.blob() })
    }

    static uploadXML(file) {
        var data = new FormData();
        data.append("xml", file);
        // Has to be a custom fetch because of Content-Type headers
        return fetch(this.makePathURL("quiz/import/"), {
            method: "POST",
            body: data
        });
    }
}

export default API;
