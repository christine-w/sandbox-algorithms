/*----------------------------------------------------------------
/ addStringNumbers2
/ Input: two string representations of integers, str1 and str2
/ Output: sum of two arguments (i.e., str1 + str2) as a string
/
/   1) adds two string representations of positive numbers
/   2) handles invalid input
/   TODO: handle negative numbers
/---------------------------------------------------------------*/
function addStringNumbers(str1, str2) {
	var sumStr = '';
	var carryOver = 0;
	
	var numDigitAdditions = Math.max(str1.length, str2.length);
	var numStr1 = '0'.repeat(numDigitAdditions-str1.length) + str1;
	var numStr2 = '0'.repeat(numDigitAdditions-str2.length) + str2;

	//console.log('numStr1: ' + numStr1 + ' numStr2: ' + numStr2 + ' numDigitAdditions: ' + numDigitAdditions);
	
	for (var i = numDigitAdditions-1; i >=0; i--) {
		var digitSum = parseInt(numStr1[i]) + parseInt(numStr2[i]) + carryOver;
		//console.log('digitSum: ' +  digitSum);
		if (isNaN(digitSum)) {
			return 'ERROR: one or more of the arguments is not a number';
		}
		sumStr = String(digitSum%10) + sumStr;
		carryOver = (digitSum - digitSum%10)/10;
		//console.log('sumStr: ' + sumStr + ' carryOver: ' + carryOver);
	}
	
	if (carryOver > 0) {
		return String(carryOver) + sumStr;
	}
	
	return sumStr;
}

exports.addStringNumbers = addStringNumbers;

// TEST CASES

console.log(addStringNumbers('0', '0')); //expect '0'
console.log(addStringNumbers('1', '0')); //expect '1'
console.log(addStringNumbers('1', '2')); //expect '3'
console.log(addStringNumbers('8', '9')); //expect '17'
console.log(addStringNumbers('8', '10')); //expect '18'
console.log(addStringNumbers('8', '19')); //expect '27'
console.log(addStringNumbers('23', '17')); //expect '40'
console.log(addStringNumbers('23', '98')); //expect '121'
console.log(addStringNumbers('10012', '99')); //expect '10111'
console.log(addStringNumbers('10000', '1')); //expect '10001'
console.log(addStringNumbers('one', '2')); //expect error message

console.log('-- Algorithms Course Week 1 Exercise --');
var a = '3141592653589793238462643383279502884197169399375105820974944592';
var b = '2718281828459045235360287471352662497757247093699959574966967627';
console.log(addStringNumbers(a,b));
