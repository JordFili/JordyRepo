import subprocess
from multiprocessing import Pool

def run_job(input_number):
    output_file = f"output_{input_number}.txt"
    with open(output_file, "w") as f:
        subprocess.run(["./hello_world", str(input_number)], stdout=f)

if __name__ == "__main__":
    with Pool(10) as p:
        p.map(run_job, range(10))