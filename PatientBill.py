import PatientClass as patc
import ProcedureClass as proc

def main():


        patient_id = 1
        name = 'Matt Jones'
        address = '123 Main st, Waco TX 76706'
        phone = '254-555-7415'
        veteran_status = 'TRUE'

        pat = patc.Patient(patient_id,name,address,phone,veteran_status)

        print('***Patient Bill***\n')
        print('Name:',pat.get_name(),'\n')
        print('Address:',pat.get_address(),'\n')
        print('Phone:',pat.get_phone())
        print('\n')


        name = 'Physical Exam'
        date = '2/15/2022'
        practitioner = 'Dr.Irvine'
        charges = 250
        patient_id = 1

        pro = proc.Procedure(name,  date, practitioner, charges, patient_id)

        print('Procedure:', pro.get_name(),'\n')
        print('Date:',pro.get_date(),'\n')
        print('Practitioner:',pro.get_practitioner(),'\n' )
        print('Charges: $',format(pro.get_charges(), ',.2f'), sep = '')

        print('\n')

        total1 = pro.get_charges()


        pro.set_name('MRI')
        pro.set_date('2/15/2022')
        pro.set_practitioner('Dr.Hamilton')
        pro.set_charges(1500)
        pro.set_patientid(1)


        print('Procedure:', pro.get_name(),'\n')
        print('Date:',pro.get_date(),'\n')
        print('Practitioner:',pro.get_practitioner(),'\n' )
        print('Charges: $',format(pro.get_charges(), ',.2f'), sep = '')

        total2 = pro.get_charges()

        print('\n')

        pro.set_name('CT Scan')
        pro.set_date('2/15/2022')
        pro.set_practitioner('Dr. Drey')
        pro.set_charges(1200)
        pro.set_patientid(2)

        if veteran_status == 'TRUE':
            total = float(total1+total2)*.6
        else:
            total = float(total1+total2)

        print('Total Charges: $', format(total, ',.2f'), sep='')





main()