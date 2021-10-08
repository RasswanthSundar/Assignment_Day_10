import unittest
from json import load
from os import path
from weekly_billing import Project,Employee

# To get the current working directory
fileloc = path.dirname(__file__)

with open(fileloc + '/test_data/employee_test_data.json') as js:
    # To store employee test data 
    emp_test_data = load(js)
    emp_test_data = emp_test_data['employee_name']

with open(fileloc + '/test_data/project_test_data.json') as js:
    # To store project test data
    pro_test_data = load(js)
    pro_test_data = pro_test_data['projects']

class EmployeeTest(unittest.TestCase):
    '''
        This calss will test the data of the two employees 
        namely {Anganandheswaran, rameezkhan} are checked with 
        the functionality of module the weekly billing 
        like the project the employee is part,
        the tags the employee is used, the total billing amount,
        the hours spent by the employee, activity summary and the project
        summary of the employee.
    '''

    def test_projects(self):
        '''
            This function will test the data of the projects 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        lst_test_project_angana = emp_test_data['Anganandheswaran']['projects']
        lst_act_project_angana = Employee('Anganandheswaran').projects_name
        lst_test_project_rameez = emp_test_data['rameezkhan']['projects']
        lst_act_project_rameez = Employee('rameezkhan').projects_name
        # Checking the data are equal or not
        self.assertListEqual(lst_act_project_angana, lst_test_project_angana)
        self.assertListEqual(lst_act_project_rameez, lst_test_project_rameez)
    
    def test_tags(self):
        '''
            This function will test the data of the tags 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        lst_test_tags_angana = emp_test_data['Anganandheswaran']['tags']
        lst_act_tags_angana = Employee('Anganandheswaran').tags
        lst_test_tags_rameez = emp_test_data['rameezkhan']['tags']
        lst_act_tags_rameez = Employee('rameezkhan').tags
        # Sorting the list since the test data is sorted
        lst_act_tags_angana.sort()
        lst_act_tags_rameez.sort()
        # Checking the data are equal or not
        self.assertListEqual(lst_act_tags_angana, lst_test_tags_angana)
        self.assertListEqual(lst_act_tags_rameez, lst_test_tags_rameez)

    def test_hours_spent(self):
        '''
            This function will test the data of the hours spent 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        total_test_time_angana = emp_test_data['Anganandheswaran']['total_hours_spent']
        total_act_time_angana = Employee('Anganandheswaran').total_hours_spent
        total_test_time_rameez = emp_test_data['rameezkhan']['total_hours_spent']
        total_act_time_rameez = Employee('rameezkhan').total_hours_spent
        # This will round off the point value to a nearest digit
        total_act_time_angana = round(total_act_time_angana, 2)
        total_act_time_rameez = round(total_act_time_rameez, 2)
        # Checking the data are equal or not
        self.assertEqual(total_act_time_angana, total_test_time_angana)
        self.assertEqual(total_act_time_rameez, total_test_time_rameez)

    def test_billing_amount(self):
        '''
            This function will test the data of the billing amount 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        billing_test_angana = emp_test_data['Anganandheswaran']['billing_amount_in_inr']
        billing_act_angana = Employee('Anganandheswaran').total_billing_in_inr
        billing_test_rameez = emp_test_data['rameezkhan']['billing_amount_in_inr']
        billing_act_rameez = Employee('rameezkhan').total_billing_in_inr
        # This will round off the point value to a nearest digit
        billing_act_angana = round(billing_act_angana)
        billing_act_rameez = round(billing_act_rameez)
        # Checking the data are equal or not
        self.assertEqual(billing_act_angana, billing_test_angana)
        self.assertEqual(billing_act_rameez, billing_test_rameez)

    def test_activity_summary(self):
        '''
            This function will test the data of the activity summary 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        dict_test_activity_angana = emp_test_data['Anganandheswaran']['activity_summary']
        dict_act_activity_angana = Employee('Anganandheswaran').calculate_activity_summary()
        dict_test_activity_rameez = emp_test_data['rameezkhan']['activity_summary']
        dict_act_activity_rameez = Employee('rameezkhan').calculate_activity_summary()
        # Checking the data are equal or not
        self.assertDictEqual(dict_act_activity_angana, dict_test_activity_angana)
        self.assertDictEqual(dict_act_activity_rameez, dict_test_activity_rameez)

    def test_project_summary(self):
        '''
            This function will test the data of the project summary 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        dict_test_project_angana = emp_test_data['Anganandheswaran']['project_summary']
        dict_act_project_angana = Employee('Anganandheswaran').calculate_project_summary()
        dict_test_project_rameez = emp_test_data['rameezkhan']['project_summary']
        dict_act_project_rameez = Employee('rameezkhan').calculate_project_summary()
        # This will round off the point value to a nearest digit
        for key in dict_act_project_angana:
            dict_act_project_angana[key] = round(dict_act_project_angana[key], 2)
        for key in dict_act_project_rameez:
            dict_act_project_rameez[key] = round(dict_act_project_rameez[key], 2)
        # Checking the data are equal or not
        self.assertDictEqual(dict_act_project_angana, dict_test_project_angana)
        self.assertDictEqual(dict_act_project_rameez, dict_test_project_rameez)

class ProjectTest(unittest.TestCase):
    '''
        This calss will test the data of the two projects 
        namely {Anganandheswaran, rameezkhan} are checked with 
        the functionality of module the weekly billing 
        like the employees in the project,
        the tags for the project is used, the total billing amount,
        the hours spent on the project, activity summary and the project
        summary of the project.
    '''

    def test_employees(self):
        '''
            This function will test the data of the employees 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        lst_test_employees_3M_CSS = pro_test_data['19210_3M_CSS']['employees']
        lst_act_employees_3M_CSS = Project('19210_3M_CSS').employees_name
        lst_test_employees_Gauge_Validation = pro_test_data['20516_Gauge Validation Project']['employees']
        lst_act_employees_Gauge_Validation = Project('20516_Gauge Validation Project').employees_name
        #convert all the list data to lower case to check
        lst_test_employees_3M_CSS = [i.lower() for i in lst_test_employees_3M_CSS]
        lst_act_employees_3M_CSS = [i.lower() for i in lst_act_employees_3M_CSS]
        lst_test_employees_Gauge_Validation = [i.lower() for i in lst_test_employees_Gauge_Validation]
        lst_act_employees_Gauge_Validation = [i.lower() for i in lst_act_employees_Gauge_Validation]
        # Sorting the list since the test data is sorted
        lst_act_employees_3M_CSS.sort()
        lst_act_employees_Gauge_Validation.sort()
        # Checking the data are equal or not
        self.assertListEqual(lst_act_employees_3M_CSS, lst_test_employees_3M_CSS)
        self.assertListEqual(lst_act_employees_Gauge_Validation, lst_test_employees_Gauge_Validation)
    
    def test_tags(self):
        '''
            This function will test the data of the tags 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        lst_test_tags_3M_CSS = pro_test_data['19210_3M_CSS']['tags']
        lst_act_tags_3M_CSS = Project('19210_3M_CSS').tags
        lst_test_tags_Gauge_Validation = pro_test_data['20516_Gauge Validation Project']['tags']
        lst_act_tags_Gauge_Validation = Project('20516_Gauge Validation Project').tags
        # Sorting the list since the test data is sorted
        lst_act_tags_3M_CSS.sort()
        lst_act_tags_Gauge_Validation.sort()
        # Checking the data are equal or not
        self.assertListEqual(lst_act_tags_3M_CSS, lst_test_tags_3M_CSS)
        self.assertListEqual(lst_act_tags_Gauge_Validation, lst_test_tags_Gauge_Validation)

    def test_hours_spent(self):
        '''
            This function will test the data of the hours spent 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        total_test_time_3M_CSS = pro_test_data['19210_3M_CSS']['total_hours_spent']
        total_act_time_3M_CSS = Project('19210_3M_CSS').total_hours_spent
        total_test_time_Gauge_Validation = pro_test_data['20516_Gauge Validation Project']['total_hours_spent']
        total_act_time_Gauge_Validation = Project('20516_Gauge Validation Project').total_hours_spent
        # This will round off the point value to a nearest digit
        total_act_time_3M_CSS = round(total_act_time_3M_CSS, 2)
        total_act_time_Gauge_Validation = round(total_act_time_Gauge_Validation, 2)
        # Checking the data are equal or not
        self.assertEqual(total_act_time_3M_CSS, total_test_time_3M_CSS)
        self.assertEqual(total_act_time_Gauge_Validation, total_test_time_Gauge_Validation)

    def test_billing_amount(self):
        '''
            This function will test the data of the billing amount 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        billing_test_3M_CSS = pro_test_data['19210_3M_CSS']['billing_amount_in_inr']
        billing_act_3M_CSS = Project('19210_3M_CSS').billing_amount_in_inr
        billing_test_Gauge_Validation = pro_test_data['20516_Gauge Validation Project']['billing_amount_in_inr']
        billing_act_Gauge_Validation = Project('20516_Gauge Validation Project').billing_amount_in_inr
        # This will round off the point value to a nearest digit
        billing_act_3M_CSS = round(billing_act_3M_CSS)
        billing_act_Gauge_Validation = round(billing_act_Gauge_Validation)
        # Checking the data are equal or not
        self.assertEqual(billing_act_3M_CSS, billing_test_3M_CSS)
        self.assertEqual(billing_act_Gauge_Validation, billing_test_Gauge_Validation)

    def test_activity_summary(self):
        '''
            This function will test the data of the activity summary 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        dict_test_activity_3M_CSS = pro_test_data['19210_3M_CSS']['activity_summary']
        dict_act_activity_3M_CSS = Project('19210_3M_CSS').calculate_activity_summary()
        dict_test_activity_Gauge_Validation = pro_test_data['20516_Gauge Validation Project']['activity_summary']
        dict_act_activity_Gauge_Validation = Project('20516_Gauge Validation Project').calculate_activity_summary()
        # This will sort the list inside the dictonary
        for key in dict_act_activity_3M_CSS:
            dict_act_activity_3M_CSS[key].sort()
        for key in dict_act_activity_Gauge_Validation:
            dict_act_activity_Gauge_Validation[key].sort()
        # Checking the data are equal or not
        self.assertDictEqual(dict_act_activity_3M_CSS, dict_test_activity_3M_CSS)
        self.assertDictEqual(dict_act_activity_Gauge_Validation, dict_test_activity_Gauge_Validation)

    def test_employee_summary(self):
        '''
            This function will test the data of the employee summary 
            from the test data from the json file generated
            and actual data from the code
        '''
        # Getting test and actual data and storing it in a variables
        dict_test_employee_3M_CSS = pro_test_data['19210_3M_CSS']['employee_summary']
        dict_act_employee_3M_CSS = Project('19210_3M_CSS').calculate_employee_summary()
        dict_test_employee_Gauge_Validation = pro_test_data['20516_Gauge Validation Project']['employee_summary']
        dict_act_employee_Gauge_Validation = Project('20516_Gauge Validation Project').calculate_employee_summary()
        # This will round off the point value to a nearest digit
        for key in dict_act_employee_3M_CSS:
            dict_act_employee_3M_CSS[key] = round(dict_act_employee_3M_CSS[key], 2)
        for key in dict_act_employee_Gauge_Validation:
            dict_act_employee_Gauge_Validation[key] = round(dict_act_employee_Gauge_Validation[key], 2)
        # Checking the data are equal or not
        self.assertDictEqual(dict_act_employee_3M_CSS, dict_test_employee_3M_CSS)
        self.assertDictEqual(dict_act_employee_Gauge_Validation, dict_test_employee_Gauge_Validation)

if __name__ == '__main__':
    unittest.main()

