from pyscript import document # type: ignore (searched it on Google)

def candidate_checker(e): 
    club_members = ["angelica delrosario", "river datiles", "aaron deguzman", "kyle delacalzada", "millicent meneses", "gilliah tabaldo", "alexandra uaje"]

    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.lower() in club_members 

    messages = (
        f'Sorry {candidate}, your name is not on the list' ,
        f'Congratulations {candidate}, you are part of the Marching Band!' 
    )

    document.getElementById('result').innerHTML = messages[member_checker]