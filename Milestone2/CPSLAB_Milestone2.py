{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "15202385-9c37-40eb-841b-2321ad6978a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pandas import DataFrame\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d6403bf7-584f-4f11-9711-ce2e3bb60e28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\caiof\\\\Desktop\\\\UnB-Semesters\\\\9-SEMESTER-HSHL\\\\AutonomousSystemsB\\\\LABCPS\\\\milestones\\\\m2'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# verify the current directory\n",
    "os.getcwd()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "af699c7f-a963-4a2c-8812-34ffcba1a5f7",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "new_dir = 'C:\\\\Users\\\\caiof\\\\Desktop\\\\UnB-Semesters\\\\9-SEMESTER-HSHL\\\\AutonomousSystemsB\\\\LABCPS\\\\milestones\\\\m2'\n",
    "os.chdir(new_dir)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "91a834da-b115-4a50-8661-8208df81aedc",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_file = open('testfile.txt', 'w')\n",
    "new_file.write('some info 123!')\n",
    "new_file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5921a583-75d9-4c31-8dbc-5dfd514a41e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'some info 123!'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_file = open('testfile.txt', 'r')\n",
    "new_file.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c6a6f30b-3e9e-4c9d-af9e-405db6d30c2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "new_file2 = open('testfile2.txt', 'w')\n",
    "new_file2.write('some info again!')\n",
    "new_file2.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6985e66c-d7d5-49cb-974a-0816e18747bf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
