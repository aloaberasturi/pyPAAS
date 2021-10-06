
from PAAS.eigentrust import ServiceEigentrust
from PAAS.assessment import Assessment
from PAAS.submission import Submission
from PAAS.peer import Peer
from experiments.syntheticMOOC import SyntheticMOOC

if __name__ == "__main__":

    # Custom vanilla experiment:

    # service = ServiceEigentrust(9)

    # referee1 = Peer('John')
    # referee1.set_as_leader(True)
    # referee2 = Peer('Don')

    # assignment1 = Submission('English Homework', 'Mike')

    # assessment1 = Assessment(referee1, assignment1, 8, None, 9)
    # assessment2 = Assessment(referee2, assignment1, 6, None, 8)

    # service.add_assessment(assessment1)
    # service.add_assessment(assessment2)


    # ---------------------- Predefined Experiments ----------------------#

    # Synthetic experiment:

    SyntheticMOOC(number_of_students = 10, n = 3, queue='ranking_MIE', informed_prior = False, percent=20)

