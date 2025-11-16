/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let l = 0, 
        r = s.length - 1;

    var alphaNum = function(c){
    return (
        (c >= 'A' && c <= 'Z') ||
        (c >= 'a' && c <= 'z') ||
        (c >= '0' && c <= '9')

    )};
    
    while (l < r){
        while (l < r && !alphaNum(s[l])){
            l++;
        }
        while (l < r && !alphaNum(s[r])){
            r--;
        }
        if (s[l].toLowerCase() !== s[r].toLowerCase()){
            return false;
        }
        l++;
        r--;
    }
    return true;

    
};