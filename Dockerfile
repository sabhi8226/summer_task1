FROM centos

RUN yum install pandas scikit-learn

COPY task1_code /* /home/

CMD python3 /home/salaryprogram.py