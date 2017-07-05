/*----------------------------------------------------------------
/ addStringNumbers
/ Input: two string representations of integers, str1 and str2
/ Output: sum of two arguments (i.e., str1 + str2) as a string
/
/   1) adds two string representations of positive numbers
/   2) handles invalid input
/   TODO: handle negative numbers
/---------------------------------------------------------------*/
function addStringNumbers(str1, str2, debug) {
	var sumStr = '';
	var carryOver = 0;
	
	var numDigitAdditions = Math.max(str1.length, str2.length);
	var numStr1 = '0'.repeat(numDigitAdditions-str1.length) + str1;
	var numStr2 = '0'.repeat(numDigitAdditions-str2.length) + str2;

	debug && console.log('numStr1: ' + numStr1 + ' numStr2: ' + numStr2 + ' numDigitAdditions: ' + numDigitAdditions);
	
	for (var i = numDigitAdditions-1; i >=0; i--) {
		var digitSum = parseInt(numStr1[i]) + parseInt(numStr2[i]) + carryOver;
		debug && console.log('digitSum: ' +  digitSum);
		if (isNaN(digitSum)) {
			return 'ERROR: one or more of the arguments is not a number';
		}
		sumStr = String(digitSum%10) + sumStr;
		carryOver = (digitSum - digitSum%10)/10;
		debug && console.log('sumStr: ' + sumStr + ' carryOver: ' + carryOver);
	}
	
	if (carryOver > 0) {
		return String(carryOver) + sumStr;
	}
	
	return sumStr;
}

function isPositiveSum(str1, str2) {
	if (str1[0] != '-' && str2[0] != '-') {
		return true;
	} else if (str1[0] == '-' && str2[0] == '-') {
		return false;
	}
	
	if (str1[0] == '-') {
		
	}
}

/*----------------------------------------------------------------
/ subtractStringNumbers
/ Input: two string representations of integers, str1 and str2
/ Output: difference from subtracting str2 from str1, as a string
/
/   1) subtracts two string representations of positive numbers
/   2) handles invalid input
/   TODO: handle negative numbers
/---------------------------------------------------------------*/

function subtractStringNumbers(str1, str2) {
	var sumStr = '';
	var carryOver = 0;

	var numDigitAdditions = Math.max(numStr1.length, numStr2.length);
	var numStr1 = '0'.repeat(numDigitAdditions-numStr1.length) + numStr1;
	var numStr2 = '0'.repeat(numDigitAdditions-numStr2.length) + numStr2;

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
	
	return sumStr

}

function isPositiveIntString(str) {
	if (str[0] === '-') {
		return false;
	}
	
	return true;
}

/*----------------------------------------------------------------
/ compareStringNumbers
/ Input: two string representations of integers, str1 and str2
/ Output: -1 if str1 < str2; 1 if str1 > str2; 0 if str1 = str2;
/
/---------------------------------------------------------------*/
function compareStringNumbers(str1, str2, debug) {
	if (str1 === str2) {
		return 0;
	}
	
	debug && console.log('str1: ' + str1 + ' str2: ' + str2);	
	var str1Sign = str1[0] === '-' ? -1 : 1;
	var str2Sign = str2[0] === '-' ? -1 : 1;
	
	if (str1Sign != str2Sign) {
		debug && console.log('different signs');
		return str1Sign;
	}

	if (str1.length > str2.length) {
		debug && console.log('same sign: ' + str1Sign + ' str1 longer');
		return str1Sign;
	} else if (str1.length < str2.length) {
		debug && console.log('same sign: ' + str1Sign + ' str1 shorter');
		return 0 - str1Sign;
	}
	
	debug && console.log('same sign, same length');
	for (var i = 0; i < str1.length; i++) {
		if (str1[i] === str2[i]) {
			continue;
		}
		var digitDiff = parseInt(str1[i]) - parseInt(str2[i]);
		if (isNaN(digitDiff)) {
			return 'ERROR: one or more of the arguments is not a number';
		}
		if (digitDiff > 0) {
			debug && console.log('same length and sign is: ' + str1Sign + ' str1 digit larger');
			return str1Sign;
			
		} 
		return 0 - str1Sign;
	}

	return 'ERROR: something went wrong with the string number comparison';
}


exports.addStringNumbers = addStringNumbers;
exports.compareStringNumbers = compareStringNumbers;

// TEST CASES

// addStringNumbers
/*
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
*/
// compareStringNumbers
var debug = false;
console.log(compareStringNumbers('0', '0', debug) + ' computed, expect 0'); //expect 0
console.log(compareStringNumbers('1', '0', debug) + ' computed, expect 1'); //expect 1
console.log(compareStringNumbers('0', '-1', debug) + ' computed, expect 1'); //expect 1
console.log(compareStringNumbers('11', '-11', debug)  + ' computed, expect 1'); //expect 1
console.log(compareStringNumbers('-11', '-12', debug)  + ' computed, expect 1'); //expect 1
console.log(compareStringNumbers('11', '12', debug)  + ' computed, expect -1'); //expect -1
console.log(compareStringNumbers('101', '10', debug)  + ' computed, expect 1'); //expect 1
console.log(compareStringNumbers('10', '101', debug)  + ' computed, expect -1'); //expect -1
console.log(compareStringNumbers('-101', '10', debug)  + ' computed, expect -1'); //expect -1
