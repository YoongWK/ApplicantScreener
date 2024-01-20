# Import the required libraries
import sys
import numpy as np
from numpy.linalg import norm
from gensim.models.doc2vec import Doc2Vec

# Main function to return match score of resume for job description
def main(resume, job_desc):
    # Load the trained Doc2Vec resume scorer model
    model = Doc2Vec.load("model/resumeScorer.model")

    # Infer document vector for resume
    v1 = model.infer_vector(resume.split())

    # Infer document vector for job description
    v2 = model.infer_vector(job_desc.split())

    # Return match score
    return f"{100*(np.dot(np.array(v1), np.array(v2))) / (norm(np.array(v1)) * norm(np.array(v2))):.0f}"

if __name__ == "__main__":
    # Print match score of resume for job description
    print(main(resume=sys.argv[1], job_desc=sys.argv[2]))