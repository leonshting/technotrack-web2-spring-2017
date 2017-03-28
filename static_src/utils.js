/**
 * Created by leonshting on 25.03.17.
 */

export function listCookies() {
    const theCookies = document.cookie.split(';');
    let aString = '';
    for (let i = 1 ; i <= theCookies.length; i++) {
        aString += i + ' ' + theCookies[i-1] + "\n";
    }
    return aString;
}

export function printHello() {
    console.log("Hello world!");
}