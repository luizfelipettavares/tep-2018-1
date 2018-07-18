var savingsAccount = {
	balance: 1000,
	interestRatePercent: 1,
	deposit: function addMoney(amount) {
		if (amount > 0) { 
			savingsAccount.balance += amount;
		}
	},
	withdraw: function removeMoney(amount) {
		var verifyBalance = savingsAccount.balance - amount;
		if (amount > 0 && verifyBalance >= 0) {
			savingsAccount.balance -= amount;
		}
	},
	summary: function printAccountSummary() {
		console.log("Welcome!\n Your Balance is currently $" + savingsAccount.balance + " and your interest rate is " + savingsAccount.interestRatePercent + "%");
	} 
};

function teste() {
	savingsAccount.summary();
	savingsAccount.deposit(350);
	savingsAccount.withdraw(475);
	savingsAccount.summary();
	savingsAccount.withdraw(200);
	savingsAccount.deposit(70);
	savingsAccount.summary();
}

teste();