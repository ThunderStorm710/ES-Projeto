function isLoggedIn(){
    console.log(sessionStorage.getItem("access") !== null && sessionStorage.getItem("access") !== "undefined");
    return sessionStorage.getItem("access") !== null && sessionStorage.getItem("access") !== "undefined";
}
export default isLoggedIn;
