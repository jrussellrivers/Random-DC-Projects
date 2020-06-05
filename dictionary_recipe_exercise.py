# Dictionary containing all of the recipe info
recipes = {
    "jrr-1":{
        "name":"Fried Chicken",
        "ingredients":[
            {
                "name":"Chicken Thighs",
                "amount":"1 lb"
            },{
                "name":"flour",
                "amount":"1 cup"
            },{
                "name":"oil",
                "amount":"3 cups"
            },{
                "name":"salt",
                "amount":"2 tbsp"
            },{
                "name":'eggs',
                'amount':'2'
            }
        ]
    },
    "jrr-2":{
        'name':'Steak',
        'ingredients':[
            {
                'name':'New York Strip',
                'amount':'12 oz'
            },{
                'name':'butter',
                'amount':'1 tbsp'
            },{
                'name':'salt',
                'amount':'2 pinches'
            },{
                'name':'pepper',
                'amount':'1 pinch'
            }
        ]
    },
    "jrr-3":{
        'name':'Fried Pork Chops',
        'ingredients':[
            {
                'name':'Boneless Pork Chops',
                'amount':'1 lb'
            },{
                'name':'Shake n\' Bake',
                'amount':'1 packet'
            },{
                'name':'oil',
                'amount':'1 cup'
            }
        ]
    }
}

# This is for if they want to restart and it covers if they dont enter an input
greeting_input = True
while greeting_input:
    greeting = input('\nWhat recipe would you like to look at? ')
    if greeting != 'jrr-1' and greeting != 'jrr-2' and greeting != 'jrr-3':
        print('\nInvalid input')

# Recipe 1

    elif greeting == 'jrr-1':
        print('\nYou have chosen to make {0}.\n'.format(recipes['jrr-1']['name']))
        
        # Thit is to list all of the ingredients
        print('You will need the following ingredients:\n')
        index = 0
        counter = 1
        for i in recipes['jrr-1']['ingredients']:
            food_name = recipes['jrr-1']['ingredients'][index]['name']
            food_amount = recipes['jrr-1']['ingredients'][index]['amount']
            print('     {0}. {1} -- {2}'.format(counter, food_name, food_amount))
            index += 1
            counter += 1
        
        # Now on to the cooking directions
        print('\nPrepare the meal as follows:')
        
        # These are to save me from copy/paste everything
        chicken = recipes['jrr-1']['ingredients'][0]['name']
        chicken_amount = recipes['jrr-1']['ingredients'][0]['amount']
        flour = recipes['jrr-1']['ingredients'][1]['name']
        flour_amount = recipes['jrr-1']['ingredients'][1]['amount']
        oil = recipes['jrr-1']['ingredients'][2]['name']
        oil_amount = recipes['jrr-1']['ingredients'][2]['amount']
        salt = recipes['jrr-1']['ingredients'][3]['name']
        salt_amount = recipes['jrr-1']['ingredients'][3]['amount']
        eggs = recipes['jrr-1']['ingredients'][4]['name']
        eggs_amount = recipes['jrr-1']['ingredients'][4]['amount']
        
        # Fried Chicken Step 1
        print('\n1. Heat {0} of {1} in a deep cast iron skillet'.format(oil_amount, oil))
        step1_chicken_input = True
        while step1_chicken_input:
            step1_chicken = input('Press \'return\' to move to the next step:')
            if step1_chicken != '':
                print('\nInvalid input')
            else:
                step1_chicken_input = False
        
        # Fried Chicken Step 2
        print('\n2. Mix {0} of {1} with {2} of {3} in one bowl and crack {4} {5} into another'.format(flour_amount, flour, salt_amount, salt, eggs_amount, eggs))
        step2_chicken_input = True
        while step2_chicken_input:
            step2_chicken = input('Press \'return\' to move to the next step:')
            if step2_chicken != '':
                print('\nInvalid input')
            else:
                step2_chicken_input = False
        
        # Fried Chicken Step 3
        print('\n3. Dredge the {0} of {1} into the {2}/{3} mixture, then into the {4}, then back into the {2}/{3}'.format(chicken_amount, chicken, flour, salt, eggs))
        step3_chicken_input = True
        while step3_chicken_input:
            step3_chicken = input('Press \'return\' to move to the next step:')
            if step3_chicken != '':
                print('\nInvalid input')
            else:
                step3_chicken_input = False

        #Fried Chicken Step 4
        print('\n4. Cook the {0} until it is a nice golden brown and has reached an internal temperature of 165 degrees'.format(chicken))
        step4_end_input = True
        while step4_end_input:
            step4_end = input('\nEnd of recipe, would you like to look up another recipe? (y/n) ')
            if step4_end != 'y' and step4_end != 'n':
                print('\nInvalid input')
            elif step4_end == 'n':
                exit()
            else:
                step4_end_input = False

# Recipe 2

    elif greeting == 'jrr-2':
        print('\nYou have chosen to make {0}.\n'.format(recipes['jrr-2']['name']))
        
        # Thit is to list all of the ingredients
        print('You will need the following ingredients:\n')
        index = 0
        counter = 1
        for i in recipes['jrr-2']['ingredients']:
            food_name = recipes['jrr-2']['ingredients'][index]['name']
            food_amount = recipes['jrr-2']['ingredients'][index]['amount']
            print('     {0}. {1} -- {2}'.format(counter, food_name, food_amount))
            index += 1
            counter += 1
        
        # Now on to the cooking directions
        print('\nPrepare the meal as follows:')
        
        # These are to save me from copy/paste everything
        meat = recipes['jrr-2']['ingredients'][0]['name']
        meat_amount = recipes['jrr-2']['ingredients'][0]['amount']
        butter = recipes['jrr-2']['ingredients'][1]['name']
        butter_amount = recipes['jrr-2']['ingredients'][1]['amount']
        salt = recipes['jrr-2']['ingredients'][2]['name']
        salt_amount = recipes['jrr-2']['ingredients'][2]['amount']
        pepper = recipes['jrr-2']['ingredients'][3]['name']
        pepper_amount = recipes['jrr-2']['ingredients'][3]['amount']
        
        # Steak Step 1
        print('\n1. Heat up cast iron skillet. Once hot, add {0} of {1}'.format(butter_amount,butter))
        step1_steak_input = True
        while step1_steak_input:
            step1_steak = input('Press \'return\' to move to the next step:')
            if step1_steak != '':
                print('\nInvalid input')
            else:
                step1_steak_input = False
        
        # Steak Step 2
        print('\n2. Season {0} of {1} with {2} of {3} and {4} of {5}'.format(meat_amount, meat, salt_amount, salt, pepper_amount, pepper))
        step2_steak_input = True
        while step2_steak_input:
            step2_steak = input('Press \'return\' to move to the next step:')
            if step2_steak != '':
                print('\nInvalid input')
            else:
                step2_steak_input = False

        # Steak Step 3
        print('\n3. Cook {0} in skillet until it reaches desired wellness'.format(meat))
        step3_end_input = True
        while step3_end_input:
            step3_end = input('\nEnd of recipe, would you like to look up another recipe? (y/n) ')
            if step3_end != 'y' and step3_end != 'n':
                print('\nInvalid input')
            elif step3_end == 'n':
                exit()
            else:
                step3_end_input = False

# Recipe 3

    elif greeting == 'jrr-3':
        print('\nYou have chosen to make {0}.\n'.format(recipes['jrr-3']['name']))
        
        # Thit is to list all of the ingredients
        print('You will need the following ingredients:\n')
        index = 0
        counter = 1
        for i in recipes['jrr-3']['ingredients']:
            food_name = recipes['jrr-3']['ingredients'][index]['name']
            food_amount = recipes['jrr-3']['ingredients'][index]['amount']
            print('     {0}. {1} -- {2}'.format(counter, food_name, food_amount))
            index += 1
            counter += 1
        
        # Now on to the cooking directions
        print('\nPrepare the meal as follows:')
        
        # These are to save me from copy/paste everything
        meat = recipes['jrr-3']['ingredients'][0]['name']
        meat_amount = recipes['jrr-3']['ingredients'][0]['amount']
        shake = recipes['jrr-3']['ingredients'][1]['name']
        shake_amount = recipes['jrr-3']['ingredients'][1]['amount']
        oil = recipes['jrr-3']['ingredients'][2]['name']
        oil_amount = recipes['jrr-3']['ingredients'][2]['amount']

        # Fried Pork Chops Step 1
        print('\n1. Heat {0} of {1} in a deep cast iron skillet'.format(oil_amount, oil))
        step1_chops_input = True
        while step1_chops_input:
            step1_chops = input('Press \'return\' to move to the next step:')
            if step1_chops != '':
                print('\nInvalid input')
            else:
                step1_chops_input = False
        
        # Fried Pork Chops Step 2
        print('\n2. Bread {0} of {1} in {2} of {3}'.format(meat_amount, meat, shake_amount, shake))
        step2_chops_input = True
        while step2_chops_input:
            step2_chops = input('Press \'return\' to move to the next step:')
            if step2_chops != '':
                print('\nInvalid input')
            else:
                step2_chops_input = False
        
        # Fried Pork Chops Step 3
        print('\n3. Cook {0} in {1} until it is a nice golden brown and has reached an internal temperature of 165 degrees'.format(meat, oil))
        step3chop_end_input = True
        while step3chop_end_input:
            step3chop_end = input('\nEnd of recipe, would you like to look up another recipe? (y/n) ')
            if step3chop_end != 'y' and step3chop_end != 'n':
                print('\nInvalid input')
            elif step3chop_end == 'n':
                exit()
            else:
                step3chop_end_input = False

# This is the end!
    else:
        greeting_input = False



