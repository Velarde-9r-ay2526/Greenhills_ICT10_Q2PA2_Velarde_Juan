from pyscript import document


grade_seven = {'gusion paxely', 'ling Arche', 'nolan Osborne'}
grade_eight = {'rias gremory', 'zero two', 'kaoruko waguri'}
grade_nine = {'ammiel velarde', 'skyler yu', 'andi santos'}
grade_ten = {'miguel velarde', 'ezekiel bacay', 'miguel piansay'}


student_list = grade_seven | grade_eight | grade_nine | grade_ten


def get_name(e):
    
    fname = document.getElementById("fname").value.lower().strip()
    lname = document.getElementById("lname").value.lower().strip()

    full_name = fname + " " + lname

    
    new_member = {full_name}
    all_members = student_list | new_member

    
    result = "<h3>All Members</h3>"

    for name in sorted(all_members):
        result += f"{name.title()}<br>"

    result += f"<br>Total members: {len(all_members)}"

    document.getElementById("result").innerHTML = result
