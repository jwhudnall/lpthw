const getInterval = (steps) => {
  return steps / 1000;
};

const getEnergy = (totalSteps, decay) => {
  let energy = 0;
  for (let i = 1; i <= totalSteps; i++) {
    if (i <= 1000) {
      energy += 1;
    } else {
      energy += (1 - decay) ** getInterval(i);
    }
  }
  return energy;
};

const result3k = getEnergy(3000, 0.046);
const result5k = getEnergy(5000, 0.046);
const result8k = getEnergy(8000, 0.046);
const result10k = getEnergy(10000, 0.046);
const result15k = getEnergy(15000, 0.046);
const result20k = getEnergy(20000, 0.046);

console.log(`Final Energy for 3,000 steps: ${result3k}`);
console.log(`Final Energy for 5,000 steps: ${result5k}`);
console.log(`Final Energy for 8,000 steps: ${result8k}`);
console.log(`Final Energy for 10,000 steps: ${result10k}`);
console.log(`Final Energy for 15,000 steps: ${result15k}`);
console.log(`Final Energy for 20,000 steps: ${result20k}`);
