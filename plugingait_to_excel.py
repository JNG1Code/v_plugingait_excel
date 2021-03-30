#!
# coding=utf-8
from __future__ import print_function

from viconnexusapi import ViconNexus
import xlsxwriter
import numpy as np
from numpy import zeros, linspace

vicon = ViconNexus.ViconNexus()

def createworksheet(ws_name, cstart, cend, cwidth):
    ws_nr = workbook.add_worksheet(ws_name)
    ws_nr.set_column(cstart, cend, cwidth)
    return ws_nr


def setbackground(sheetname):
    normal = workbook.add_format({'font_name': 'Calibri'})
    # normal.set_bg_color('#EDF2F4')
    data = (
        '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
        '',
        '', '', '', '', '')
    sheetname.write_column('A1', data, normal)
    sheetname.write_column('B1', data, normal)
    sheetname.write_column('C1', data, normal)
    sheetname.write_column('D1', data, normal)
    sheetname.write_column('E1', data, normal)
    sheetname.write_column('F1', data, normal)
    sheetname.write_column('G1', data, normal)
    sheetname.write_column('H1', data, normal)
    sheetname.write_column('I1', data, normal)


def writedataexcel(inputname, sheetname, tabcolor):
    row = 1
    col = 0
    for row, array in enumerate(inputname):
        for col, value in enumerate(array):
            sheetname.write(col + 1, row, value)
    sheetname.set_tab_color(tabcolor)


def worksheet_headings_kinem(worksheet):
    # Insert worksheet col headings
    worksheet.write('B1', 'LPelvisAngles_X', boldleft)
    worksheet.write('C1', 'LPelvisAngles_Y', boldleft)
    worksheet.write('D1', 'LPelvisAngles_Z', boldleft)
    worksheet.write('E1', 'RPelvisAngles_X', boldright)
    worksheet.write('F1', 'RPelvisAngles_Y', boldright)
    worksheet.write('G1', 'RPelvisAngles_Z', boldright)
    worksheet.write('H1', 'LHipAngles_X', boldleft)
    worksheet.write('I1', 'LHipAngles_Y', boldleft)
    worksheet.write('J1', 'LHipAngles_Z', boldleft)
    worksheet.write('K1', 'RHipAngles_X', boldright)
    worksheet.write('L1', 'RHipAngles_Y', boldright)
    worksheet.write('M1', 'RHipAngles_Z', boldright)
    worksheet.write('N1', 'LKneeAngles_X', boldleft)
    worksheet.write('O1', 'LKneeAngles_Y', boldleft)
    worksheet.write('P1', 'LKneeAngles_Z', boldleft)
    worksheet.write('Q1', 'RKneeAngles_X', boldright)
    worksheet.write('R1', 'RKneeAngles_Y', boldright)
    worksheet.write('S1', 'RKneeAngles_Z', boldright)
    worksheet.write('T1', 'LAnkleAngles_X', boldleft)
    worksheet.write('U1', 'LAnkleAngles_Y', boldleft)
    worksheet.write('V1', 'LAnkleAngles_Z', boldleft)
    worksheet.write('W1', 'RAnkleAngles_X', boldright)
    worksheet.write('X1', 'RAnkleAngles_Y', boldright)
    worksheet.write('Y1', 'RAnkleAngles_Z', boldright)
    worksheet.write('Z1', 'LFootProgressAngles_X', boldleft)
    worksheet.write('AA1', 'LFootProgressAngles_Y', boldleft)
    worksheet.write('AB1', 'LFootProgressAngles_Z', boldleft)
    worksheet.write('AC1', 'RFootProgressAngles_X', boldright)
    worksheet.write('AD1', 'RFootProgressAngles_Y', boldright)
    worksheet.write('AE1', 'RFootProgressAngles_Z', boldright)
    worksheet.write('AF1', 'LHeadAngles_X', boldleft)
    worksheet.write('AG1', 'LHeadAngles_Y', boldleft)
    worksheet.write('AH1', 'LHeadAngles_Z', boldleft)
    worksheet.write('AI1', 'RHeadAngles_X', boldright)
    worksheet.write('AJ1', 'RHeadAngles_Y', boldright)
    worksheet.write('AK1', 'RHeadAngles_Z', boldright)
    worksheet.write('AL1', 'LThoraxAngles_X', boldleft)
    worksheet.write('AM1', 'LThoraxAngles_Y', boldleft)
    worksheet.write('AN1', 'LThoraxAngles_Z', boldleft)
    worksheet.write('AO1', 'RThoraxAngles_X', boldright)
    worksheet.write('AP1', 'RThoraxAngles_Y', boldright)
    worksheet.write('AQ1', 'RThoraxAngles_Z', boldright)
    worksheet.write('AR1', 'LNeckAngles_X', boldleft)
    worksheet.write('AS1', 'LNeckAngles_Y', boldleft)
    worksheet.write('AT1', 'LNeckAngles_Z', boldleft)
    worksheet.write('AU1', 'RNeckAngles_X', boldright)
    worksheet.write('AV1', 'RNeckAngles_Y', boldright)
    worksheet.write('AW1', 'RNeckAngles_Z', boldright)
    worksheet.write('AX1', 'LSpineAngles_X', boldleft)
    worksheet.write('AY1', 'LSpineAngles_Y', boldleft)
    worksheet.write('AZ1', 'LSpineAngles_Z', boldleft)
    worksheet.write('BA1', 'RSpineAngles_X', boldright)
    worksheet.write('BB1', 'RSpineAngles_Y', boldright)
    worksheet.write('BC1', 'RSpineAngles_Z', boldright)
    worksheet.write('BD1', 'LShoulderAngles_X', boldleft)
    worksheet.write('BE1', 'LShoulderAngles_Y', boldleft)
    worksheet.write('BF1', 'LShoulderAngles_Z', boldleft)
    worksheet.write('BG1', 'RShoulderAngles_X', boldright)
    worksheet.write('BH1', 'RShoulderAngles_Y', boldright)
    worksheet.write('BI1', 'RShoulderAngles_Z', boldright)
    worksheet.write('BJ1', 'LElbowAngles_X', boldleft)
    worksheet.write('BK1', 'LElbowAngles_Y', boldleft)
    worksheet.write('BL1', 'LElbowAngles_Z', boldleft)
    worksheet.write('BM1', 'RElbowAngles_X', boldright)
    worksheet.write('BN1', 'RElbowAngles_Y', boldright)
    worksheet.write('BO1', 'RElbowAngles_Z', boldright)
    worksheet.write('BP1', 'LWristAngles_X', boldleft)
    worksheet.write('BQ1', 'LWristAngles_Y', boldleft)
    worksheet.write('BR1', 'LWristAngles_Z', boldleft)
    worksheet.write('BS1', 'RWristAngles_X', boldright)
    worksheet.write('BT1', 'RWristAngles_Y', boldright)
    worksheet.write('BU1', 'RWristAngles_Z', boldright)


def worksheet_headings_kine(worksheet):
    worksheet.write('B1', 'LHipMoment_X', boldleft)
    worksheet.write('C1', 'LHipMoment_Y', boldleft)
    worksheet.write('D1', 'LHipMoment_Z', boldleft)
    worksheet.write('E1', 'LHipPower_Z', boldleft)
    worksheet.write('F1', 'RHipMoment_X', boldright)
    worksheet.write('G1', 'RHipMoment_Y', boldright)
    worksheet.write('H1', 'RHipMoment_Z', boldright)
    worksheet.write('I1', 'RHipPower_Z', boldright)
    worksheet.write('J1', 'LKneeMoment_X', boldleft)
    worksheet.write('K1', 'LKneeMoment_Y', boldleft)
    worksheet.write('L1', 'LKneeMoment_Z', boldleft)
    worksheet.write('M1', 'LKneePower_Z', boldleft)
    worksheet.write('N1', 'RKneeMoment_X', boldright)
    worksheet.write('O1', 'RKneeMoment_Y', boldright)
    worksheet.write('P1', 'RKneeMoment_Z', boldright)
    worksheet.write('Q1', 'RKneePower_Z', boldright)
    worksheet.write('R1', 'LAnkleMoment_X', boldleft)
    worksheet.write('S1', 'LAnkleMoment_Y', boldleft)
    worksheet.write('T1', 'LAnkleMoment_Z', boldleft)
    worksheet.write('U1', 'LAnklePower_Z', boldleft)
    worksheet.write('V1', 'RAnkleMoment_X', boldright)
    worksheet.write('W1', 'RAnkleMoment_Y', boldright)
    worksheet.write('X1', 'RAnkleMoment_Z', boldright)
    worksheet.write('Y1', 'RAnklePower_Z', boldright)


def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros


def subjparam(name, input_name_a, input_name_b, sheetname, cell_location_a, cell_location_b, cell_location_c):
    if input_name_a or input_name_b in SubjParamOutputs:
        input_name_a = vicon.GetSubjectParamDetails(SubjectName, input_name_a)[0]
        input_name_b = vicon.GetSubjectParamDetails(SubjectName, input_name_b)[0]
        sheetname.write(cell_location_a, name, bold)
        sheetname.write(cell_location_b, input_name_a, normal)
        sheetname.write(cell_location_c, input_name_b, normal)
    else:
        sheetname.write(cell_location_a, name, bold)
        sheetname.write(cell_location_b, '', normal)
        sheetname.write(cell_location_c, '', normal)


def analysisout(name, input_name_a, input_name_b, sheetname, cell_location_a, cell_location_b, cell_location_c):
    if input_name_a or input_name_b in AnalysisOutputs:
        input_name_a = vicon.GetAnalysisParamDetails(SubjectName, input_name_a)[0]
        input_name_b = vicon.GetAnalysisParamDetails(SubjectName, input_name_b)[0]
        sheetname.write(cell_location_a, name, bold)
        sheetname.write(cell_location_b, input_name_a, normal)
        sheetname.write(cell_location_c, input_name_b, normal)
    else:
        sheetname.write(cell_location_a, name, bold)
        sheetname.write(cell_location_b, '', normal)
        sheetname.write(cell_location_c, '', normal)


def createnormchart(x_axis, Left_y_axis, Right_y_axis, chart_Title, yUnit, miny, maxy, interval):
    line_chart = workbook.add_chart(dict(type='scatter', subtype='straight'))
    line_chart.add_series(
        dict(name='Left', categories=x_axis, values=Left_y_axis,
             line={'color': '#CC0C0C'}))  # Configure the first series.
    line_chart.add_series(
        dict(name='Right', categories=x_axis, values=Right_y_axis,
             line={'color': '#053C5E'}))  # Configure second series. Note use of alternative syntax to define ranges.
    line_chart.set_title(
        dict(name=chart_Title, name_font={'size': 12, }))  # Add a chart title and some axis labels.
    line_chart.set_x_axis(
        dict(name='Percentage of Gait Cycle', name_font={'size': 8, }, min=0, max=100, interval_unit=20))
    line_chart.set_y_axis(
        dict(name=yUnit, name_font={'size': 8, }, major_gridlines={'visible': False, }, min=miny, max=maxy,
             interval_unit=interval))
    line_chart.set_style(2)  # Set an Excel chart style. Colors with white outline and shadow.
    return line_chart


def data_GaitCycleCount(subj):
    left_cycle_count = len(vicon.GetEvents(subj, "Left", "Foot Strike")[0]) - 1
    if left_cycle_count <= 0:
        left_cycle_count = 0

    right_cycle_count = len(vicon.GetEvents(subj, "Right", "Foot Strike")[0]) - 1
    if right_cycle_count <= 0:
        right_cycle_count = 0

    print ("Left Gait Cycle Count: %s" % left_cycle_count)
    print ("Right Gait Cycle Count: %s" % right_cycle_count)

    return left_cycle_count, right_cycle_count


def data_Norm_Kinematics_Left(f_strike=None, left_cycle_count=None, data_Input_Angle="Requested Angle_left"):
    # type: (object, object, object) -> object
    if left_cycle_count == 1 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        norm_x = np.interp(tn, gc1t, data_x1)
        norm_y = np.interp(tn, gc1t, data_y1)
        norm_z = np.interp(tn, gc1t, data_z1)
        norm_x2 = zerolistmaker(100)
        norm_y2 = zerolistmaker(100)
        norm_z2 = zerolistmaker(100)
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)

        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif left_cycle_count == 2 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = data_y[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = data_z[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        norm_x = (np.array(norm_x1) + np.array(norm_x2)) / 2
        norm_y = (np.array(norm_y1) + np.array(norm_y2)) / 2
        norm_z = (np.array(norm_z1) + np.array(norm_z2)) / 2
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif left_cycle_count == 3 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = data_y[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = data_z[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = data_y[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = data_z[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3)) / 3
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3)) / 3
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3)) / 3
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif left_cycle_count == 4 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        f_strike5 = f_strike[4:5]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gait_cycle4 = []
        gait_cycle4 += f_strike4[0], f_strike5[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        gc4 = data_x[min(gait_cycle4):max(gait_cycle4)]
        gc4t = np.linspace(0, 100, len(gc4))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = data_y[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = data_z[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = data_y[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = data_z[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        data_x4 = data_x[min(gait_cycle4):max(gait_cycle4)]
        data_y4 = data_y[min(gait_cycle4):max(gait_cycle4)]
        data_z4 = data_z[min(gait_cycle4):max(gait_cycle4)]
        norm_x4 = np.interp(tn, gc4t, data_x4)
        norm_y4 = np.interp(tn, gc4t, data_y4)
        norm_z4 = np.interp(tn, gc4t, data_z4)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3) + np.array(norm_x4)) / 4
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3) + np.array(norm_y4)) / 4
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3) + np.array(norm_z4)) / 4
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif left_cycle_count >= 5 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        f_strike5 = f_strike[4:5]
        f_strike6 = f_strike[5:6]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gait_cycle4 = []
        gait_cycle4 += f_strike4[0], f_strike5[0]
        gait_cycle5 = []
        gait_cycle5 += f_strike5[0], f_strike6[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        gc4 = data_x[min(gait_cycle4):max(gait_cycle4)]
        gc4t = np.linspace(0, 100, len(gc4))
        gc5 = data_x[min(gait_cycle5):max(gait_cycle5)]
        gc5t = np.linspace(0, 100, len(gc5))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = data_y[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = data_z[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = data_y[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = data_z[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        data_x4 = data_x[min(gait_cycle4):max(gait_cycle4)]
        data_y4 = data_y[min(gait_cycle4):max(gait_cycle4)]
        data_z4 = data_z[min(gait_cycle4):max(gait_cycle4)]
        norm_x4 = np.interp(tn, gc4t, data_x4)
        norm_y4 = np.interp(tn, gc4t, data_y4)
        norm_z4 = np.interp(tn, gc4t, data_z4)
        data_x5 = data_x[min(gait_cycle5):max(gait_cycle5)]
        data_y5 = data_y[min(gait_cycle5):max(gait_cycle5)]
        data_z5 = data_z[min(gait_cycle5):max(gait_cycle5)]
        norm_x5 = np.interp(tn, gc5t, data_x5)
        norm_y5 = np.interp(tn, gc5t, data_y5)
        norm_z5 = np.interp(tn, gc5t, data_z5)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3) + np.array(norm_x4) + np.array(
            norm_x5)) / 5
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3) + np.array(norm_y4) + np.array(
            norm_y5)) / 5
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3) + np.array(norm_z4) + np.array(
            norm_z5)) / 5
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    else:
        norm_x = zerolistmaker(100)
        norm_y = zerolistmaker(100)
        norm_z = zerolistmaker(100)
        norm_x1 = zerolistmaker(100)
        norm_y1 = zerolistmaker(100)
        norm_z1 = zerolistmaker(100)
        norm_x2 = zerolistmaker(100)
        norm_y2 = zerolistmaker(100)
        norm_z2 = zerolistmaker(100)
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]


def data_Norm_Kinetics_Left(f_strike=None, left_cycle_count=None, data_Input_Angle="Requested Angle_left"):
    tn = linspace(1, 100, 101)
    myInt = 1000
    if left_cycle_count == 1 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        norm_x = (np.array(norm_x1))
        norm_y = (np.array(norm_y1))
        norm_z = (np.array(norm_z1))
        norm_x2 = zerolistmaker(100)
        norm_y2 = zerolistmaker(100)
        norm_z2 = zerolistmaker(100)
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif left_cycle_count == 2 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = dataMY[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = dataMZ[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        norm_x = (np.array(norm_x1) + np.array(norm_x2)) / 2
        norm_y = (np.array(norm_y1) + np.array(norm_y2)) / 2
        norm_z = (np.array(norm_z1) + np.array(norm_z2)) / 2
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif left_cycle_count == 3 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = dataMY[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = dataMZ[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = dataMY[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = dataMZ[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3)) / 3
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3)) / 3
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3)) / 3
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif left_cycle_count == 4 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        f_strike5 = f_strike[4:5]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gait_cycle4 = []
        gait_cycle4 += f_strike4[0], f_strike5[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        gc4 = dataMX[min(gait_cycle4):max(gait_cycle4)]
        gc4t = np.linspace(0, 100, len(gc4))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = dataMY[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = dataMZ[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = dataMY[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = dataMZ[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        data_x4 = dataMX[min(gait_cycle4):max(gait_cycle4)]
        data_y4 = dataMY[min(gait_cycle4):max(gait_cycle4)]
        data_z4 = dataMZ[min(gait_cycle4):max(gait_cycle4)]
        norm_x4 = np.interp(tn, gc4t, data_x4)
        norm_y4 = np.interp(tn, gc4t, data_y4)
        norm_z4 = np.interp(tn, gc4t, data_z4)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3) + np.array(norm_x4)) / 4
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3) + np.array(norm_y4)) / 4
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3) + np.array(norm_z4)) / 4
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif left_cycle_count >= 5 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        f_strike5 = f_strike[4:5]
        f_strike6 = f_strike[5:6]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gait_cycle4 = []
        gait_cycle4 += f_strike4[0], f_strike5[0]
        gait_cycle5 = []
        gait_cycle5 += f_strike5[0], f_strike6[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        gc4 = dataMX[min(gait_cycle4):max(gait_cycle4)]
        gc4t = np.linspace(0, 100, len(gc4))
        gc5 = dataMX[min(gait_cycle5):max(gait_cycle5)]
        gc5t = np.linspace(0, 100, len(gc5))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = dataMY[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = dataMZ[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = dataMY[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = dataMZ[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        data_x4 = dataMX[min(gait_cycle4):max(gait_cycle4)]
        data_y4 = dataMY[min(gait_cycle4):max(gait_cycle4)]
        data_z4 = dataMZ[min(gait_cycle4):max(gait_cycle4)]
        norm_x4 = np.interp(tn, gc4t, data_x4)
        norm_y4 = np.interp(tn, gc4t, data_y4)
        norm_z4 = np.interp(tn, gc4t, data_z4)
        data_x5 = dataMX[min(gait_cycle5):max(gait_cycle5)]
        data_y5 = dataMY[min(gait_cycle5):max(gait_cycle5)]
        data_z5 = dataMZ[min(gait_cycle5):max(gait_cycle5)]
        norm_x5 = np.interp(tn, gc5t, data_x5)
        norm_y5 = np.interp(tn, gc5t, data_y5)
        norm_z5 = np.interp(tn, gc5t, data_z5)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3) +
                  np.array(norm_x4) + np.array(norm_x5)) / 5
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3) +
                  np.array(norm_y4) + np.array(norm_y5)) / 5
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3) +
                  np.array(norm_z4) + np.array(norm_z5)) / 5
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    else:
        norm_x = zerolistmaker(100)
        norm_y = zerolistmaker(100)
        norm_z = zerolistmaker(100)
        return [norm_x, norm_y, norm_z]


def data_Norm_Kinematics_Right(f_strike=None, right_cycle_count=None, data_Input_Angle="Requested Angle_right"):
    if right_cycle_count == 1 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        norm_x = np.interp(tn, gc1t, data_x1)
        norm_y = np.interp(tn, gc1t, data_y1)
        norm_z = np.interp(tn, gc1t, data_z1)
        norm_x2 = zerolistmaker(100)
        norm_y2 = zerolistmaker(100)
        norm_z2 = zerolistmaker(100)
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif right_cycle_count == 2 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = data_y[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = data_z[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        norm_x = (np.array(norm_x1) + np.array(norm_x2)) / 2
        norm_y = (np.array(norm_y1) + np.array(norm_y2)) / 2
        norm_z = (np.array(norm_z1) + np.array(norm_z2)) / 2
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif right_cycle_count == 3 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = data_y[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = data_z[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = data_y[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = data_z[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3)) / 3
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3)) / 3
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3)) / 3
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif right_cycle_count == 4 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        f_strike5 = f_strike[4:5]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gait_cycle4 = []
        gait_cycle4 += f_strike4[0], f_strike5[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        gc4 = data_x[min(gait_cycle4):max(gait_cycle4)]
        gc4t = np.linspace(0, 100, len(gc4))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = data_y[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = data_z[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = data_y[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = data_z[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        data_x4 = data_x[min(gait_cycle4):max(gait_cycle4)]
        data_y4 = data_y[min(gait_cycle4):max(gait_cycle4)]
        data_z4 = data_z[min(gait_cycle4):max(gait_cycle4)]
        norm_x4 = np.interp(tn, gc4t, data_x4)
        norm_y4 = np.interp(tn, gc4t, data_y4)
        norm_z4 = np.interp(tn, gc4t, data_z4)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3) + np.array(norm_x4)) / 4
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3) + np.array(norm_y4)) / 4
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3) + np.array(norm_z4)) / 4
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif right_cycle_count >= 5 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        tn = linspace(1, 100, 101)
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        f_strike5 = f_strike[4:5]
        f_strike6 = f_strike[5:6]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gait_cycle4 = []
        gait_cycle4 += f_strike4[0], f_strike5[0]
        gait_cycle5 = []
        gait_cycle5 += f_strike5[0], f_strike6[0]
        gc1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        gc4 = data_x[min(gait_cycle4):max(gait_cycle4)]
        gc4t = np.linspace(0, 100, len(gc4))
        gc5 = data_x[min(gait_cycle5):max(gait_cycle5)]
        gc5t = np.linspace(0, 100, len(gc5))
        data_x1 = data_x[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = data_y[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = data_z[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = data_x[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = data_y[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = data_z[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = data_x[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = data_y[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = data_z[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        data_x4 = data_x[min(gait_cycle4):max(gait_cycle4)]
        data_y4 = data_y[min(gait_cycle4):max(gait_cycle4)]
        data_z4 = data_z[min(gait_cycle4):max(gait_cycle4)]
        norm_x4 = np.interp(tn, gc4t, data_x4)
        norm_y4 = np.interp(tn, gc4t, data_y4)
        norm_z4 = np.interp(tn, gc4t, data_z4)
        data_x5 = data_x[min(gait_cycle5):max(gait_cycle5)]
        data_y5 = data_y[min(gait_cycle5):max(gait_cycle5)]
        data_z5 = data_z[min(gait_cycle5):max(gait_cycle5)]
        norm_x5 = np.interp(tn, gc5t, data_x5)
        norm_y5 = np.interp(tn, gc5t, data_y5)
        norm_z5 = np.interp(tn, gc5t, data_z5)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3) + np.array(norm_x4) + np.array(
            norm_x5)) / 5
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3) + np.array(norm_y4) + np.array(
            norm_y5)) / 5
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3) + np.array(norm_z4) + np.array(
            norm_z5)) / 5
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    else:
        norm_x = zerolistmaker(100)
        norm_y = zerolistmaker(100)
        norm_z = zerolistmaker(100)
        norm_x1 = zerolistmaker(100)
        norm_y1 = zerolistmaker(100)
        norm_z1 = zerolistmaker(100)
        norm_x2 = zerolistmaker(100)
        norm_y2 = zerolistmaker(100)
        norm_z2 = zerolistmaker(100)
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]


def data_Norm_Kinetics_Right(f_strike=None, right_cycle_count=None, data_Input_Angle="Requested Angle_right"):
    tn = linspace(1, 100, 101)
    myInt = 1000
    tn = linspace(1, 100, 101)
    myInt = 1000
    if right_cycle_count == 1 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        norm_x = (np.array(norm_x1))
        norm_y = (np.array(norm_y1))
        norm_z = (np.array(norm_z1))
        norm_x2 = zerolistmaker(100)
        norm_y2 = zerolistmaker(100)
        norm_z2 = zerolistmaker(100)
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif right_cycle_count == 2 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = dataMY[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = dataMZ[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        norm_x = (np.array(norm_x1) + np.array(norm_x2)) / 2
        norm_y = (np.array(norm_y1) + np.array(norm_y2)) / 2
        norm_z = (np.array(norm_z1) + np.array(norm_z2)) / 2
        norm_x3 = zerolistmaker(100)
        norm_y3 = zerolistmaker(100)
        norm_z3 = zerolistmaker(100)
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif right_cycle_count == 3 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = dataMY[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = dataMZ[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = dataMY[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = dataMZ[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3)) / 3
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3)) / 3
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3)) / 3
        norm_x4 = zerolistmaker(100)
        norm_y4 = zerolistmaker(100)
        norm_z4 = zerolistmaker(100)
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif right_cycle_count == 4 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        f_strike5 = f_strike[4:5]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gait_cycle4 = []
        gait_cycle4 += f_strike4[0], f_strike5[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        gc4 = dataMX[min(gait_cycle4):max(gait_cycle4)]
        gc4t = np.linspace(0, 100, len(gc4))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = dataMY[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = dataMZ[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = dataMY[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = dataMZ[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        data_x4 = dataMX[min(gait_cycle4):max(gait_cycle4)]
        data_y4 = dataMY[min(gait_cycle4):max(gait_cycle4)]
        data_z4 = dataMZ[min(gait_cycle4):max(gait_cycle4)]
        norm_x4 = np.interp(tn, gc4t, data_x4)
        norm_y4 = np.interp(tn, gc4t, data_y4)
        norm_z4 = np.interp(tn, gc4t, data_z4)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3) + np.array(norm_x4)) / 4
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3) + np.array(norm_y4)) / 4
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3) + np.array(norm_z4)) / 4
        norm_x5 = zerolistmaker(100)
        norm_y5 = zerolistmaker(100)
        norm_z5 = zerolistmaker(100)
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    elif right_cycle_count >= 5 and data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        f_strike1 = f_strike[:1]
        f_strike2 = f_strike[1:2]
        f_strike3 = f_strike[2:3]
        f_strike4 = f_strike[3:4]
        f_strike5 = f_strike[4:5]
        f_strike6 = f_strike[5:6]
        gait_cycle1 = []
        gait_cycle1 += f_strike1[0], f_strike2[0]
        gait_cycle2 = []
        gait_cycle2 += f_strike2[0], f_strike3[0]
        gait_cycle3 = []
        gait_cycle3 += f_strike3[0], f_strike4[0]
        gait_cycle4 = []
        gait_cycle4 += f_strike4[0], f_strike5[0]
        gait_cycle5 = []
        gait_cycle5 += f_strike5[0], f_strike6[0]
        gc1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        gc1t = np.linspace(0, 100, len(gc1))
        gc2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        gc2t = np.linspace(0, 100, len(gc2))
        gc3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        gc3t = np.linspace(0, 100, len(gc3))
        gc4 = dataMX[min(gait_cycle4):max(gait_cycle4)]
        gc4t = np.linspace(0, 100, len(gc4))
        gc5 = dataMX[min(gait_cycle5):max(gait_cycle5)]
        gc5t = np.linspace(0, 100, len(gc5))
        data_x1 = dataMX[min(gait_cycle1):max(gait_cycle1)]
        data_y1 = dataMY[min(gait_cycle1):max(gait_cycle1)]
        data_z1 = dataMZ[min(gait_cycle1):max(gait_cycle1)]
        norm_x1 = np.interp(tn, gc1t, data_x1)
        norm_y1 = np.interp(tn, gc1t, data_y1)
        norm_z1 = np.interp(tn, gc1t, data_z1)
        data_x2 = dataMX[min(gait_cycle2):max(gait_cycle2)]
        data_y2 = dataMY[min(gait_cycle2):max(gait_cycle2)]
        data_z2 = dataMZ[min(gait_cycle2):max(gait_cycle2)]
        norm_x2 = np.interp(tn, gc2t, data_x2)
        norm_y2 = np.interp(tn, gc2t, data_y2)
        norm_z2 = np.interp(tn, gc2t, data_z2)
        data_x3 = dataMX[min(gait_cycle3):max(gait_cycle3)]
        data_y3 = dataMY[min(gait_cycle3):max(gait_cycle3)]
        data_z3 = dataMZ[min(gait_cycle3):max(gait_cycle3)]
        norm_x3 = np.interp(tn, gc3t, data_x3)
        norm_y3 = np.interp(tn, gc3t, data_y3)
        norm_z3 = np.interp(tn, gc3t, data_z3)
        data_x4 = dataMX[min(gait_cycle4):max(gait_cycle4)]
        data_y4 = dataMY[min(gait_cycle4):max(gait_cycle4)]
        data_z4 = dataMZ[min(gait_cycle4):max(gait_cycle4)]
        norm_x4 = np.interp(tn, gc4t, data_x4)
        norm_y4 = np.interp(tn, gc4t, data_y4)
        norm_z4 = np.interp(tn, gc4t, data_z4)
        data_x5 = dataMX[min(gait_cycle5):max(gait_cycle5)]
        data_y5 = dataMY[min(gait_cycle5):max(gait_cycle5)]
        data_z5 = dataMZ[min(gait_cycle5):max(gait_cycle5)]
        norm_x5 = np.interp(tn, gc5t, data_x5)
        norm_y5 = np.interp(tn, gc5t, data_y5)
        norm_z5 = np.interp(tn, gc5t, data_z5)
        norm_x = (np.array(norm_x1) + np.array(norm_x2) + np.array(norm_x3) +
                  np.array(norm_x4) + np.array(norm_x5)) / 5
        norm_y = (np.array(norm_y1) + np.array(norm_y2) + np.array(norm_y3) +
                  np.array(norm_y4) + np.array(norm_y5)) / 5
        norm_z = (np.array(norm_z1) + np.array(norm_z2) + np.array(norm_z3) +
                  np.array(norm_z4) + np.array(norm_z5)) / 5
        return [norm_x, norm_y, norm_z, norm_x1, norm_y1, norm_z1, norm_x2, norm_y2, norm_z2, norm_x3, norm_y3, norm_z3,
                norm_x4, norm_y4, norm_z4, norm_x5, norm_y5, norm_z5]

    else:
        norm_x = zerolistmaker(100)
        norm_y = zerolistmaker(100)
        norm_z = zerolistmaker(100)
        return [norm_x, norm_y, norm_z]


def data_PugInGait(data_Input_Angle="Requested Angle_left"):
    if data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
    else:
        print(data_Input_Angle + " not present converted to zero")
        # data_a = zerolistmaker(100)
        data_x = zerolistmaker(100)
        data_y = zerolistmaker(100)
        data_z = zerolistmaker(100)
    return data_x, data_y, data_z


def data_PlugInGait_power(data_Input_Angle):
    if data_Input_Angle in ModelOutputs:
        dataPZ = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)][0][0][2])
    else:
        dataPZ = zeros(empty)
    return dataPZ


def data_PlugInGait_moments(data_Input_Angle):
    myInt = 1000
    if data_Input_Angle in ModelOutputs:
        data_a = ([vicon.GetModelOutput(SubjectName, data_Input_Angle)])
        data_x = data_a[0][0][0]
        data_y = data_a[0][0][1]
        data_z = data_a[0][0][2]
        dataMX = [i / myInt for i in data_x]
        dataMY = [i / myInt for i in data_y]
        dataMZ = [i / myInt for i in data_z]
        return dataMX, dataMY, dataMZ


def data_Kinematics():
    Frames = vicon.GetFrameCount()
    Range = Frames + 1
    TrialFrames = list(range(1, Range, 1))

    Kinematics = [TrialFrames, LPelvisX, LPelvisY, LPelvisZ, RPelvisX, RPelvisY, RPelvisZ,
                  LHipX, LHipY, LHipZ, RHipX, RHipY, RHipZ,
                  LKneeX, LKneeY, LKneeZ, RKneeX, RKneeY, RKneeZ,
                  LAnkleX, LAnkleY, LAnkleZ, RAnkleX, RAnkleY, RAnkleZ,
                  LFootProX, LFootProY, LFootProZ, RFootProX, RFootProY, RFootProZ,
                  LHeadAnglesX, LHeadAnglesY, LHeadAnglesZ, RHeadAnglesX, RHeadAnglesY, RHeadAnglesZ,
                  LThoraxAnglesX, LThoraxAnglesY, LThoraxAnglesZ, RThoraxAnglesX, RThoraxAnglesY, RThoraxAnglesZ,
                  LNeckAnglesX, LNeckAnglesY, LNeckAnglesZ, RNeckAnglesX, RNeckAnglesY, RNeckAnglesZ,
                  LSpineAnglesX, LSpineAnglesY, LSpineAnglesZ, RSpineAnglesX, RSpineAnglesY, RSpineAnglesZ,
                  LShoulderAnglesX, LShoulderAnglesY, LShoulderAnglesZ, RShoulderAnglesX, RShoulderAnglesY,
                  RShoulderAnglesZ,
                  LElbowAnglesX, LElbowAnglesY, LElbowAnglesZ, RElbowAnglesX, RElbowAnglesY, RElbowAnglesZ,
                  LWristAnglesX, LWristAnglesY, Norm_LWristAnglesZ, RWristAnglesX, RWristAnglesY, Norm_RWristAnglesZ]

    return Kinematics


def data_Kinetics():
    Frames = vicon.GetFrameCount()
    Range = Frames + 1
    TrialFrames = list(range(1, Range, 1))

    Kinetics = [TrialFrames, LHipMXD, LHipMYD, LHipMZD, LHipPZ, RHipMXD, RHipMYD, RHipMZD, RHipPZ, LKneeMXD, LKneeMYD,
                LKneeMZD, LKneePZ, RKneeMXD, RKneeMYD, RKneeMZD, RKneePZ, LAnkMXD, LAnkMYD, LAnkMZD, LAnkPZ, RAnkMXD,
                RAnkMYD, RAnkMZD, RAnkPZ]

    return Kinetics


def data_NormKinetics():
    Percentage = list(range(0, 101, 1))

    NormKinetics = [Percentage,
                    Norm_LHipMX, Norm_LHipMY, Norm_LHipMZ, Norm_TLHipPZ, Norm_RHipMX, Norm_RHipMY, Norm_RHipMZ,
                    Norm_TRHipPZ,
                    Norm_LKneeMX, Norm_LKneeMY, Norm_LKneeMZ, Norm_TLKneePZ, Norm_RKneeMX, Norm_RKneeMY, Norm_RKneeMZ,
                    Norm_TRKneePZ,
                    Norm_LAnkleMX, Norm_LAnkleMY, Norm_LAnkleMZ, Norm_TLAnklePZ, Norm_RAnkleMX, Norm_RAnkleMY,
                    Norm_RAnkleMZ, Norm_TRAnklePZ]

    return NormKinetics


def data_NormKinetics1():
    Percentage = list(range(0, 101, 1))

    NormKinetics = [Percentage,
                    Norm_LHipMX1, Norm_LHipMY1, Norm_LHipMZ1, Norm_TLHipPZ1, Norm_RHipMX1, Norm_RHipMY1, Norm_RHipMZ1,
                    Norm_TRHipPZ1,
                    Norm_LKneeMX1, Norm_LKneeMY1, Norm_LKneeMZ1, Norm_TLKneePZ1, Norm_RKneeMX1, Norm_RKneeMY1,
                    Norm_RKneeMZ1,
                    Norm_TRKneePZ1,
                    Norm_LAnkleMX1, Norm_LAnkleMY1, Norm_LAnkleMZ1, Norm_TLAnklePZ1, Norm_RAnkleMX1, Norm_RAnkleMY1,
                    Norm_RAnkleMZ1, Norm_TRAnklePZ1]

    return NormKinetics


def data_NormKinetics2():
    Percentage = list(range(0, 101, 1))

    NormKinetics = [Percentage,
                    Norm_LHipMX2, Norm_LHipMY2, Norm_LHipMZ2, Norm_TLHipPZ2, Norm_RHipMX2, Norm_RHipMY2, Norm_RHipMZ2,
                    Norm_TRHipPZ2, Norm_LKneeMX2, Norm_LKneeMY2, Norm_LKneeMZ2, Norm_TLKneePZ2, Norm_RKneeMX2,
                    Norm_RKneeMY2,
                    Norm_RKneeMZ2, Norm_TRKneePZ2, Norm_LAnkleMX2, Norm_LAnkleMY2, Norm_LAnkleMZ2, Norm_TLAnklePZ2,
                    Norm_RAnkleMX2, Norm_RAnkleMY2, Norm_RAnkleMZ2, Norm_TRAnklePZ2]

    return NormKinetics


def data_NormKinetics3():
    Percentage = list(range(0, 101, 1))

    NormKinetics = [Percentage,
                    Norm_LHipMX3, Norm_LHipMY3, Norm_LHipMZ3, Norm_TLHipPZ3, Norm_RHipMX3, Norm_RHipMY3, Norm_RHipMZ3,
                    Norm_TRHipPZ3, Norm_LKneeMX3, Norm_LKneeMY3, Norm_LKneeMZ3, Norm_TLKneePZ3, Norm_RKneeMX3,
                    Norm_RKneeMY3,
                    Norm_RKneeMZ3, Norm_TRKneePZ3, Norm_LAnkleMX3, Norm_LAnkleMY3, Norm_LAnkleMZ3, Norm_TLAnklePZ3,
                    Norm_RAnkleMX3, Norm_RAnkleMY3, Norm_RAnkleMZ3, Norm_TRAnklePZ3]

    return NormKinetics


def data_NormKinetics4():
    Percentage = list(range(0, 101, 1))

    NormKinetics = [Percentage,
                    Norm_LHipMX4, Norm_LHipMY4, Norm_LHipMZ4, Norm_TLHipPZ4, Norm_RHipMX4, Norm_RHipMY4, Norm_RHipMZ4,
                    Norm_TRHipPZ4, Norm_LKneeMX4, Norm_LKneeMY4, Norm_LKneeMZ4, Norm_TLKneePZ4, Norm_RKneeMX4,
                    Norm_RKneeMY4,
                    Norm_RKneeMZ4, Norm_TRKneePZ4, Norm_LAnkleMX4, Norm_LAnkleMY4, Norm_LAnkleMZ4, Norm_TLAnklePZ4,
                    Norm_RAnkleMX4, Norm_RAnkleMY4, Norm_RAnkleMZ4, Norm_TRAnklePZ4]

    return NormKinetics


def data_NormKinetics5():
    Percentage = list(range(0, 101, 1))

    NormKinetics = [Percentage,
                    Norm_LHipMX5, Norm_LHipMY5, Norm_LHipMZ5, Norm_TLHipPZ5, Norm_RHipMX5, Norm_RHipMY5, Norm_RHipMZ5,
                    Norm_TRHipPZ5, Norm_LKneeMX5, Norm_LKneeMY5, Norm_LKneeMZ5, Norm_TLKneePZ5, Norm_RKneeMX5,
                    Norm_RKneeMY5,
                    Norm_RKneeMZ5, Norm_TRKneePZ5, Norm_LAnkleMX5, Norm_LAnkleMY5, Norm_LAnkleMZ5, Norm_TLAnklePZ5,
                    Norm_RAnkleMX5, Norm_RAnkleMY5, Norm_RAnkleMZ5, Norm_TRAnklePZ5]

    return NormKinetics


def data_NormKinematics():
    Percentage = list(range(0, 101, 1))

    NormKinematics = [Percentage,
                      Norm_LPelvisX, Norm_LPelvisY, Norm_LPelvisZ, Norm_RPelvisX, Norm_RPelvisY, Norm_RPelvisZ,
                      Norm_LHipX, Norm_LHipY, Norm_LHipZ, Norm_RHipX, Norm_RHipY, Norm_RHipZ,
                      Norm_LKneeX, Norm_LKneeY, Norm_LKneeZ, Norm_RKneeX, Norm_RKneeY, Norm_RKneeZ,
                      Norm_LAnkleX, Norm_LAnkleY, Norm_LAnkleZ, Norm_RAnkleX, Norm_RAnkleY, Norm_RAnkleZ,
                      Norm_LFootProX, Norm_LFootProY, Norm_LFootProZ, Norm_RFootProX, Norm_RFootProY, Norm_RFootProZ,
                      Norm_LHeadAnglesX, Norm_LHeadAnglesY, Norm_LHeadAnglesZ, Norm_RHeadAnglesX, Norm_RHeadAnglesY,
                      Norm_RHeadAnglesZ,
                      Norm_LThoraxAnglesX, Norm_LThoraxAnglesY, Norm_LThoraxAnglesZ, Norm_RThoraxAnglesX,
                      Norm_RThoraxAnglesY, Norm_RThoraxAnglesZ,
                      Norm_LNeckAnglesX, Norm_LNeckAnglesY, Norm_LNeckAnglesZ, Norm_RNeckAnglesX, Norm_RNeckAnglesY,
                      Norm_RNeckAnglesZ,
                      Norm_LSpineAnglesX, Norm_LSpineAnglesY, Norm_LSpineAnglesZ, Norm_RSpineAnglesX,
                      Norm_RSpineAnglesY, Norm_RSpineAnglesZ,
                      Norm_LShoulderAnglesX, Norm_LShoulderAnglesY, Norm_LShoulderAnglesZ, Norm_RShoulderAnglesX,
                      Norm_RShoulderAnglesY, Norm_RShoulderAnglesZ,
                      Norm_LElbowAnglesX, Norm_LElbowAnglesY, Norm_LElbowAnglesZ, Norm_RElbowAnglesX,
                      Norm_RElbowAnglesY, Norm_RElbowAnglesZ,
                      Norm_LWristAnglesX, Norm_LWristAnglesY, Norm_LWristAnglesZ, Norm_RWristAnglesX,
                      Norm_RWristAnglesY, Norm_RWristAnglesZ]

    return NormKinematics


def data_NormKinematics1():
    Percentage = list(range(0, 101, 1))

    NormKinematics = [Percentage,
                      Norm_LPelvisX1, Norm_LPelvisY1, Norm_LPelvisZ1, Norm_RPelvisX1, Norm_RPelvisY1, Norm_RPelvisZ1,
                      Norm_LHipX1, Norm_LHipY1, Norm_LHipZ1, Norm_RHipX1, Norm_RHipY1, Norm_RHipZ1,
                      Norm_LKneeX1, Norm_LKneeY1, Norm_LKneeZ1, Norm_RKneeX1, Norm_RKneeY1, Norm_RKneeZ1,
                      Norm_LAnkleX1, Norm_LAnkleY1, Norm_LAnkleZ1, Norm_RAnkleX1, Norm_RAnkleY1, Norm_RAnkleZ1,
                      Norm_LFootProX1, Norm_LFootProY1, Norm_LFootProZ1, Norm_RFootProX1, Norm_RFootProY1,
                      Norm_RFootProZ1,
                      Norm_LHeadAnglesX1, Norm_LHeadAnglesY1, Norm_LHeadAnglesZ1, Norm_RHeadAnglesX1,
                      Norm_RHeadAnglesY1,
                      Norm_RHeadAnglesZ1,
                      Norm_LThoraxAnglesX1, Norm_LThoraxAnglesY1, Norm_LThoraxAnglesZ1, Norm_RThoraxAnglesX1,
                      Norm_RThoraxAnglesY1, Norm_RThoraxAnglesZ1,
                      Norm_LNeckAnglesX1, Norm_LNeckAnglesY1, Norm_LNeckAnglesZ1, Norm_RNeckAnglesX1,
                      Norm_RNeckAnglesY1,
                      Norm_RNeckAnglesZ1,
                      Norm_LSpineAnglesX1, Norm_LSpineAnglesY1, Norm_LSpineAnglesZ1, Norm_RSpineAnglesX1,
                      Norm_RSpineAnglesY1, Norm_RSpineAnglesZ1,
                      Norm_LShoulderAnglesX1, Norm_LShoulderAnglesY1, Norm_LShoulderAnglesZ1, Norm_RShoulderAnglesX1,
                      Norm_RShoulderAnglesY1, Norm_RShoulderAnglesZ1,
                      Norm_LElbowAnglesX1, Norm_LElbowAnglesY1, Norm_LElbowAnglesZ1, Norm_RElbowAnglesX1,
                      Norm_RElbowAnglesY1, Norm_RElbowAnglesZ1,
                      Norm_LWristAnglesX1, Norm_LWristAnglesY1, Norm_LWristAnglesZ1, Norm_RWristAnglesX1,
                      Norm_RWristAnglesY1, Norm_RWristAnglesZ1]

    return NormKinematics


def data_NormKinematics2():
    Percentage = list(range(0, 101, 1))

    NormKinematics = [Percentage,
                      Norm_LPelvisX2, Norm_LPelvisY2, Norm_LPelvisZ2, Norm_RPelvisX2, Norm_RPelvisY2, Norm_RPelvisZ2,
                      Norm_LHipX2, Norm_LHipY2, Norm_LHipZ2, Norm_RHipX2, Norm_RHipY2, Norm_RHipZ2,
                      Norm_LKneeX2, Norm_LKneeY2, Norm_LKneeZ2, Norm_RKneeX2, Norm_RKneeY2, Norm_RKneeZ2,
                      Norm_LAnkleX2, Norm_LAnkleY2, Norm_LAnkleZ2, Norm_RAnkleX2, Norm_RAnkleY2, Norm_RAnkleZ2,
                      Norm_LFootProX2, Norm_LFootProY2, Norm_LFootProZ2, Norm_RFootProX2, Norm_RFootProY2,
                      Norm_RFootProZ2,
                      Norm_LHeadAnglesX2, Norm_LHeadAnglesY2, Norm_LHeadAnglesZ2, Norm_RHeadAnglesX2,
                      Norm_RHeadAnglesY2,
                      Norm_RHeadAnglesZ2,
                      Norm_LThoraxAnglesX2, Norm_LThoraxAnglesY2, Norm_LThoraxAnglesZ2, Norm_RThoraxAnglesX2,
                      Norm_RThoraxAnglesY2, Norm_RThoraxAnglesZ2,
                      Norm_LNeckAnglesX2, Norm_LNeckAnglesY2, Norm_LNeckAnglesZ2, Norm_RNeckAnglesX2,
                      Norm_RNeckAnglesY2,
                      Norm_RNeckAnglesZ2,
                      Norm_LSpineAnglesX2, Norm_LSpineAnglesY2, Norm_LSpineAnglesZ2, Norm_RSpineAnglesX2,
                      Norm_RSpineAnglesY2, Norm_RSpineAnglesZ2,
                      Norm_LShoulderAnglesX2, Norm_LShoulderAnglesY2, Norm_LShoulderAnglesZ2, Norm_RShoulderAnglesX2,
                      Norm_RShoulderAnglesY2, Norm_RShoulderAnglesZ2,
                      Norm_LElbowAnglesX2, Norm_LElbowAnglesY2, Norm_LElbowAnglesZ2, Norm_RElbowAnglesX2,
                      Norm_RElbowAnglesY2, Norm_RElbowAnglesZ2,
                      Norm_LWristAnglesX2, Norm_LWristAnglesY2, Norm_LWristAnglesZ2, Norm_RWristAnglesX2,
                      Norm_RWristAnglesY2, Norm_RWristAnglesZ2]

    return NormKinematics


def data_NormKinematics3():
    Percentage = list(range(0, 101, 1))

    NormKinematics = [Percentage,
                      Norm_LPelvisX3, Norm_LPelvisY3, Norm_LPelvisZ3, Norm_RPelvisX3, Norm_RPelvisY3, Norm_RPelvisZ3,
                      Norm_LHipX3, Norm_LHipY3, Norm_LHipZ3, Norm_RHipX3, Norm_RHipY3, Norm_RHipZ3,
                      Norm_LKneeX3, Norm_LKneeY3, Norm_LKneeZ3, Norm_RKneeX3, Norm_RKneeY3, Norm_RKneeZ3,
                      Norm_LAnkleX3, Norm_LAnkleY3, Norm_LAnkleZ3, Norm_RAnkleX3, Norm_RAnkleY3, Norm_RAnkleZ3,
                      Norm_LFootProX3, Norm_LFootProY3, Norm_LFootProZ3, Norm_RFootProX3, Norm_RFootProY3,
                      Norm_RFootProZ3,
                      Norm_LHeadAnglesX3, Norm_LHeadAnglesY3, Norm_LHeadAnglesZ3, Norm_RHeadAnglesX3,
                      Norm_RHeadAnglesY3,
                      Norm_RHeadAnglesZ3,
                      Norm_LThoraxAnglesX3, Norm_LThoraxAnglesY3, Norm_LThoraxAnglesZ3, Norm_RThoraxAnglesX3,
                      Norm_RThoraxAnglesY3, Norm_RThoraxAnglesZ3,
                      Norm_LNeckAnglesX3, Norm_LNeckAnglesY3, Norm_LNeckAnglesZ3, Norm_RNeckAnglesX3,
                      Norm_RNeckAnglesY3,
                      Norm_RNeckAnglesZ3,
                      Norm_LSpineAnglesX3, Norm_LSpineAnglesY3, Norm_LSpineAnglesZ3, Norm_RSpineAnglesX3,
                      Norm_RSpineAnglesY3, Norm_RSpineAnglesZ3,
                      Norm_LShoulderAnglesX3, Norm_LShoulderAnglesY3, Norm_LShoulderAnglesZ3, Norm_RShoulderAnglesX3,
                      Norm_RShoulderAnglesY3, Norm_RShoulderAnglesZ3,
                      Norm_LElbowAnglesX3, Norm_LElbowAnglesY3, Norm_LElbowAnglesZ3, Norm_RElbowAnglesX3,
                      Norm_RElbowAnglesY3, Norm_RElbowAnglesZ3,
                      Norm_LWristAnglesX3, Norm_LWristAnglesY3, Norm_LWristAnglesZ3, Norm_RWristAnglesX3,
                      Norm_RWristAnglesY3, Norm_RWristAnglesZ3]

    return NormKinematics


def data_NormKinematics4():
    Percentage = list(range(0, 101, 1))

    NormKinematics = [Percentage,
                      Norm_LPelvisX4, Norm_LPelvisY4, Norm_LPelvisZ4, Norm_RPelvisX4, Norm_RPelvisY4, Norm_RPelvisZ4,
                      Norm_LHipX4, Norm_LHipY4, Norm_LHipZ4, Norm_RHipX4, Norm_RHipY4, Norm_RHipZ4,
                      Norm_LKneeX4, Norm_LKneeY4, Norm_LKneeZ4, Norm_RKneeX4, Norm_RKneeY4, Norm_RKneeZ4,
                      Norm_LAnkleX4, Norm_LAnkleY4, Norm_LAnkleZ4, Norm_RAnkleX4, Norm_RAnkleY4, Norm_RAnkleZ4,
                      Norm_LFootProX4, Norm_LFootProY4, Norm_LFootProZ4, Norm_RFootProX4, Norm_RFootProY4,
                      Norm_RFootProZ4,
                      Norm_LHeadAnglesX4, Norm_LHeadAnglesY4, Norm_LHeadAnglesZ4, Norm_RHeadAnglesX4,
                      Norm_RHeadAnglesY4,
                      Norm_RHeadAnglesZ4,
                      Norm_LThoraxAnglesX4, Norm_LThoraxAnglesY4, Norm_LThoraxAnglesZ4, Norm_RThoraxAnglesX4,
                      Norm_RThoraxAnglesY4, Norm_RThoraxAnglesZ4,
                      Norm_LNeckAnglesX4, Norm_LNeckAnglesY4, Norm_LNeckAnglesZ4, Norm_RNeckAnglesX4,
                      Norm_RNeckAnglesY4,
                      Norm_RNeckAnglesZ4,
                      Norm_LSpineAnglesX4, Norm_LSpineAnglesY4, Norm_LSpineAnglesZ4, Norm_RSpineAnglesX4,
                      Norm_RSpineAnglesY4, Norm_RSpineAnglesZ4,
                      Norm_LShoulderAnglesX4, Norm_LShoulderAnglesY4, Norm_LShoulderAnglesZ4, Norm_RShoulderAnglesX4,
                      Norm_RShoulderAnglesY4, Norm_RShoulderAnglesZ4,
                      Norm_LElbowAnglesX4, Norm_LElbowAnglesY4, Norm_LElbowAnglesZ4, Norm_RElbowAnglesX4,
                      Norm_RElbowAnglesY4, Norm_RElbowAnglesZ4,
                      Norm_LWristAnglesX4, Norm_LWristAnglesY4, Norm_LWristAnglesZ4, Norm_RWristAnglesX4,
                      Norm_RWristAnglesY4, Norm_RWristAnglesZ4]

    return NormKinematics


def data_NormKinematics5():
    Percentage = list(range(0, 101, 1))

    NormKinematics = [Percentage,
                      Norm_LPelvisX5, Norm_LPelvisY5, Norm_LPelvisZ5, Norm_RPelvisX5, Norm_RPelvisY5, Norm_RPelvisZ5,
                      Norm_LHipX5, Norm_LHipY5, Norm_LHipZ5, Norm_RHipX5, Norm_RHipY5, Norm_RHipZ5,
                      Norm_LKneeX5, Norm_LKneeY5, Norm_LKneeZ5, Norm_RKneeX5, Norm_RKneeY5, Norm_RKneeZ5,
                      Norm_LAnkleX5, Norm_LAnkleY5, Norm_LAnkleZ5, Norm_RAnkleX5, Norm_RAnkleY5, Norm_RAnkleZ5,
                      Norm_LFootProX5, Norm_LFootProY5, Norm_LFootProZ5, Norm_RFootProX5, Norm_RFootProY5,
                      Norm_RFootProZ5,
                      Norm_LHeadAnglesX5, Norm_LHeadAnglesY5, Norm_LHeadAnglesZ5, Norm_RHeadAnglesX5,
                      Norm_RHeadAnglesY5,
                      Norm_RHeadAnglesZ5,
                      Norm_LThoraxAnglesX5, Norm_LThoraxAnglesY5, Norm_LThoraxAnglesZ5, Norm_RThoraxAnglesX5,
                      Norm_RThoraxAnglesY5, Norm_RThoraxAnglesZ5,
                      Norm_LNeckAnglesX5, Norm_LNeckAnglesY5, Norm_LNeckAnglesZ5, Norm_RNeckAnglesX5,
                      Norm_RNeckAnglesY5,
                      Norm_RNeckAnglesZ5,
                      Norm_LSpineAnglesX5, Norm_LSpineAnglesY5, Norm_LSpineAnglesZ5, Norm_RSpineAnglesX5,
                      Norm_RSpineAnglesY5, Norm_RSpineAnglesZ5,
                      Norm_LShoulderAnglesX5, Norm_LShoulderAnglesY5, Norm_LShoulderAnglesZ5, Norm_RShoulderAnglesX5,
                      Norm_RShoulderAnglesY5, Norm_RShoulderAnglesZ5,
                      Norm_LElbowAnglesX5, Norm_LElbowAnglesY5, Norm_LElbowAnglesZ5, Norm_RElbowAnglesX5,
                      Norm_RElbowAnglesY5, Norm_RElbowAnglesZ5,
                      Norm_LWristAnglesX5, Norm_LWristAnglesY5, Norm_LWristAnglesZ5, Norm_RWristAnglesX5,
                      Norm_RWristAnglesY5, Norm_RWristAnglesZ5]

    return NormKinematics


def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros


def data_NormZero(data_Input_Angle):
    print(data_Input_Angle + " not present converted to zero")
    data_x = zerolistmaker(101)
    data_y = zerolistmaker(101)
    data_z = zerolistmaker(101)
    return data_x, data_y, data_z


# Extract information from active trial

SubjectName = vicon.GetSubjectNames()[0]
SessionLoc = vicon.GetTrialName()[0]
TrialName = SessionLoc + vicon.GetTrialName()[1]
TrialName1 = vicon.GetTrialName()[1]
Frames = vicon.GetFrameCount()
empty = (4, Frames)
ModelOutputs = vicon.GetModelOutputNames(SubjectName)
LeftStrike = vicon.GetEvents(SubjectName, 'Left', 'Foot Strike')[0]
RightStrike = vicon.GetEvents(SubjectName, 'Right', 'Foot Strike')[0]

AnalysisOutputs = vicon.GetAnalysisParamNames(SubjectName)
SubjParamOutputs = vicon.GetSubjectParamNames(SubjectName)

left_gait_cycle, right_gait_cycle = data_GaitCycleCount(SubjectName)

if left_gait_cycle >= 1:
    Norm_LPelvisX, Norm_LPelvisY, Norm_LPelvisZ, Norm_LPelvisX1, Norm_LPelvisY1, Norm_LPelvisZ1, \
        Norm_LPelvisX2, Norm_LPelvisY2, Norm_LPelvisZ2, Norm_LPelvisX3, Norm_LPelvisY3, Norm_LPelvisZ3, Norm_LPelvisX4, Norm_LPelvisY4, Norm_LPelvisZ4, \
        Norm_LPelvisX5, Norm_LPelvisY5, Norm_LPelvisZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LPelvisAngles")

    Norm_LHipX, Norm_LHipY, Norm_LHipZ, Norm_LHipX1, Norm_LHipY1, Norm_LHipZ1, Norm_LHipX2, Norm_LHipY2, Norm_LHipZ2, \
        Norm_LHipX3, Norm_LHipY3, Norm_LHipZ3, Norm_LHipX4, Norm_LHipY4, Norm_LHipZ4, \
        Norm_LHipX5, Norm_LHipY5, Norm_LHipZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LHipAngles")

    Norm_LKneeX, Norm_LKneeY, Norm_LKneeZ, Norm_LKneeX1, Norm_LKneeY1, Norm_LKneeZ1, Norm_LKneeX2, Norm_LKneeY2, Norm_LKneeZ2, \
        Norm_LKneeX3, Norm_LKneeY3, Norm_LKneeZ3, Norm_LKneeX4, Norm_LKneeY4, Norm_LKneeZ4, Norm_LKneeX5, Norm_LKneeY5, Norm_LKneeZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LKneeAngles")

    Norm_LAnkleX, Norm_LAnkleY, Norm_LAnkleZ, Norm_LAnkleX1, Norm_LAnkleY1, Norm_LAnkleZ1, Norm_LAnkleX2, Norm_LAnkleY2, Norm_LAnkleZ2, \
        Norm_LAnkleX3, Norm_LAnkleY3, Norm_LAnkleZ3, Norm_LAnkleX4, Norm_LAnkleY4, Norm_LAnkleZ4, \
        Norm_LAnkleX5, Norm_LAnkleY5, Norm_LAnkleZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LAnkleAngles")

    Norm_LFootProX, Norm_LFootProY, Norm_LFootProZ, Norm_LFootProX1, Norm_LFootProY1, Norm_LFootProZ1, Norm_LFootProX2, Norm_LFootProY2, Norm_LFootProZ2, \
        Norm_LFootProX3, Norm_LFootProY3, Norm_LFootProZ3, Norm_LFootProX4, Norm_LFootProY4, Norm_LFootProZ4, \
        Norm_LFootProX5, Norm_LFootProY5, Norm_LFootProZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LFootProgressAngles")

    Norm_LHeadAnglesX, Norm_LHeadAnglesY, Norm_LHeadAnglesZ, Norm_LHeadAnglesX1, Norm_LHeadAnglesY1, Norm_LHeadAnglesZ1, Norm_LHeadAnglesX2, Norm_LHeadAnglesY2, Norm_LHeadAnglesZ2, \
        Norm_LHeadAnglesX3, Norm_LHeadAnglesY3, Norm_LHeadAnglesZ3, Norm_LHeadAnglesX4, Norm_LHeadAnglesY4, Norm_LHeadAnglesZ4, \
        Norm_LHeadAnglesX5, Norm_LHeadAnglesY5, Norm_LHeadAnglesZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LHeadAngles")

    Norm_LThoraxAnglesX, Norm_LThoraxAnglesY, Norm_LThoraxAnglesZ, Norm_LThoraxAnglesX1, Norm_LThoraxAnglesY1, Norm_LThoraxAnglesZ1, \
        Norm_LThoraxAnglesX2, Norm_LThoraxAnglesY2, Norm_LThoraxAnglesZ2, Norm_LThoraxAnglesX3, Norm_LThoraxAnglesY3, Norm_LThoraxAnglesZ3, \
        Norm_LThoraxAnglesX4, Norm_LThoraxAnglesY4, Norm_LThoraxAnglesZ4, Norm_LThoraxAnglesX5, Norm_LThoraxAnglesY5, Norm_LThoraxAnglesZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LThoraxAngles")

    Norm_LNeckAnglesX, Norm_LNeckAnglesY, Norm_LNeckAnglesZ, Norm_LNeckAnglesX1, Norm_LNeckAnglesY1, Norm_LNeckAnglesZ1, \
        Norm_LNeckAnglesX2, Norm_LNeckAnglesY2, Norm_LNeckAnglesZ2, Norm_LNeckAnglesX3, Norm_LNeckAnglesY3, Norm_LNeckAnglesZ3, \
        Norm_LNeckAnglesX4, Norm_LNeckAnglesY4, Norm_LNeckAnglesZ4, Norm_LNeckAnglesX5, Norm_LNeckAnglesY5, Norm_LNeckAnglesZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LNeckAngles")

    Norm_LSpineAnglesX, Norm_LSpineAnglesY, Norm_LSpineAnglesZ, Norm_LSpineAnglesX1, Norm_LSpineAnglesY1, Norm_LSpineAnglesZ1, \
        Norm_LSpineAnglesX2, Norm_LSpineAnglesY2, Norm_LSpineAnglesZ2, Norm_LSpineAnglesX3, Norm_LSpineAnglesY3, Norm_LSpineAnglesZ3, \
        Norm_LSpineAnglesX4, Norm_LSpineAnglesY4, Norm_LSpineAnglesZ4, Norm_LSpineAnglesX5, Norm_LSpineAnglesY5, Norm_LSpineAnglesZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LSpineAngles")

    Norm_LShoulderAnglesX, Norm_LShoulderAnglesY, Norm_LShoulderAnglesZ, Norm_LShoulderAnglesX1, Norm_LShoulderAnglesY1, Norm_LShoulderAnglesZ1, \
        Norm_LShoulderAnglesX2, Norm_LShoulderAnglesY2, Norm_LShoulderAnglesZ2, Norm_LShoulderAnglesX3, Norm_LShoulderAnglesY3, Norm_LShoulderAnglesZ3, \
        Norm_LShoulderAnglesX4, Norm_LShoulderAnglesY4, Norm_LShoulderAnglesZ4, Norm_LShoulderAnglesX5, Norm_LShoulderAnglesY5, Norm_LShoulderAnglesZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LShoulderAngles")

    Norm_LElbowAnglesX, Norm_LElbowAnglesY, Norm_LElbowAnglesZ, Norm_LElbowAnglesX1, Norm_LElbowAnglesY1, Norm_LElbowAnglesZ1, \
        Norm_LElbowAnglesX2, Norm_LElbowAnglesY2, Norm_LElbowAnglesZ2, Norm_LElbowAnglesX3, Norm_LElbowAnglesY3, Norm_LElbowAnglesZ3, \
        Norm_LElbowAnglesX4, Norm_LElbowAnglesY4, Norm_LElbowAnglesZ4, Norm_LElbowAnglesX5, Norm_LElbowAnglesY5, Norm_LElbowAnglesZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LElbowAngles")

    Norm_LWristAnglesX, Norm_LWristAnglesY, Norm_LWristAnglesZ, Norm_LWristAnglesX1, Norm_LWristAnglesY1, Norm_LWristAnglesZ1, \
        Norm_LWristAnglesX2, Norm_LWristAnglesY2, Norm_LWristAnglesZ2, Norm_LWristAnglesX3, Norm_LWristAnglesY3, Norm_LWristAnglesZ3, \
        Norm_LWristAnglesX4, Norm_LWristAnglesY4, Norm_LWristAnglesZ4, Norm_LWristAnglesX5, Norm_LWristAnglesY5, Norm_LWristAnglesZ5 \
        = data_Norm_Kinematics_Left(LeftStrike, left_gait_cycle, "LWristAngles")

    Norm_LHipMX, Norm_LHipMY, Norm_LHipMZ, Norm_LHipMX1, Norm_LHipMY1, Norm_LHipMZ1, \
        Norm_LHipMX2, Norm_LHipMY2, Norm_LHipMZ2, Norm_LHipMX3, Norm_LHipMY3, Norm_LHipMZ3, \
        Norm_LHipMX4, Norm_LHipMY4, Norm_LHipMZ4, Norm_LHipMX5, Norm_LHipMY5, Norm_LHipMZ5 \
        = data_Norm_Kinetics_Left(LeftStrike, left_gait_cycle, 'LHipMoment')

    Norm_TLHipPX, Norm_TLHipPY, Norm_TLHipPZ, Norm_TLHipPX1, Norm_TLHipPY1, Norm_TLHipPZ1, \
        Norm_TLHipPX2, Norm_TLHipPY2, Norm_TLHipPZ2, Norm_TLHipPX3, Norm_TLHipPY3, Norm_TLHipPZ3, \
        Norm_TLHipPX4, Norm_TLHipPY4, Norm_TLHipPZ4, Norm_TLHipPX5, Norm_TLHipPY5, Norm_TLHipPZ5 \
        = data_Norm_Kinetics_Left(LeftStrike, left_gait_cycle, 'LHipPower')

    Norm_LKneeMX, Norm_LKneeMY, Norm_LKneeMZ, Norm_LKneeMX1, Norm_LKneeMY1, Norm_LKneeMZ1, \
        Norm_LKneeMX2, Norm_LKneeMY2, Norm_LKneeMZ2, Norm_LKneeMX3, Norm_LKneeMY3, Norm_LKneeMZ3, \
        Norm_LKneeMX4, Norm_LKneeMY4, Norm_LKneeMZ4, Norm_LKneeMX5, Norm_LKneeMY5, Norm_LKneeMZ5 \
        = data_Norm_Kinetics_Left(LeftStrike, left_gait_cycle, 'LKneeMoment')

    Norm_TLKneePX, Norm_TLKneePY, Norm_TLKneePZ, Norm_TLKneePX1, Norm_TLKneePY1, Norm_TLKneePZ1, \
        Norm_TLKneePX2, Norm_TLKneePY2, Norm_TLKneePZ2, Norm_TLKneePX3, Norm_TLKneePY3, Norm_TLKneePZ3, \
        Norm_TLKneePX4, Norm_TLKneePY4, Norm_TLKneePZ4, Norm_TLKneePX5, Norm_TLKneePY5, Norm_TLKneePZ5 \
        = data_Norm_Kinetics_Left(LeftStrike, left_gait_cycle, 'LKneePower')

    Norm_LAnkleMX, Norm_LAnkleMY, Norm_LAnkleMZ, Norm_LAnkleMX1, Norm_LAnkleMY1, Norm_LAnkleMZ1, \
        Norm_LAnkleMX2, Norm_LAnkleMY2, Norm_LAnkleMZ2, Norm_LAnkleMX3, Norm_LAnkleMY3, Norm_LAnkleMZ3, \
        Norm_LAnkleMX4, Norm_LAnkleMY4, Norm_LAnkleMZ4, Norm_LAnkleMX5, Norm_LAnkleMY5, Norm_LAnkleMZ5 \
        = data_Norm_Kinetics_Left(LeftStrike, left_gait_cycle, 'LAnkleMoment')

    Norm_TLAnklePX, Norm_TLAnklePY, Norm_TLAnklePZ, Norm_TLAnklePX1, Norm_TLAnklePY1, Norm_TLAnklePZ1, \
        Norm_TLAnklePX2, Norm_TLAnklePY2, Norm_TLAnklePZ2, Norm_TLAnklePX3, Norm_TLAnklePY3, Norm_TLAnklePZ3, \
        Norm_TLAnklePX4, Norm_TLAnklePY4, Norm_TLAnklePZ4, Norm_TLAnklePX5, Norm_TLAnklePY5, Norm_TLAnklePZ5 \
        = data_Norm_Kinetics_Left(LeftStrike, left_gait_cycle, 'LAnklePower')


else:
    Norm_LPelvisX, Norm_LPelvisY, Norm_LPelvisZ, Norm_LPelvisX1, Norm_LPelvisY1, Norm_LPelvisZ1, \
        Norm_LPelvisX2, Norm_LPelvisY2, Norm_LPelvisZ2, Norm_LPelvisX3, Norm_LPelvisY3, Norm_LPelvisZ3, \
        Norm_LPelvisX4, Norm_LPelvisY4, Norm_LPelvisZ4, Norm_LPelvisX5, Norm_LPelvisY5, Norm_LPelvisZ5 \
        = data_NormZero("LPelvisAngles")

    Norm_LHipX, Norm_LHipY, Norm_LHipZ, Norm_LHipX1, Norm_LHipY1, Norm_LHipZ1, Norm_LHipX2, Norm_LHipY2, Norm_LHipZ2, \
        Norm_LHipX3, Norm_LHipY3, Norm_LHipZ3, Norm_LHipX4, Norm_LHipY4, Norm_LHipZ4, \
        Norm_LHipX5, Norm_LHipY5, Norm_LHipZ5 \
        = data_NormZero("LHipAngles")

    Norm_LKneeX, Norm_LKneeY, Norm_LKneeZ, Norm_LKneeX1, Norm_LKneeY1, Norm_LKneeZ1, Norm_LKneeX2, Norm_LKneeY2, Norm_LKneeZ2, \
        Norm_LKneeX3, Norm_LKneeY3, Norm_LKneeZ3, Norm_LKneeX4, Norm_LKneeY4, Norm_LKneeZ4, \
        Norm_LKneeX5, Norm_LKneeY5, Norm_LKneeZ5 \
        = data_NormZero("LKneeAngles")

    Norm_LAnkleX, Norm_LAnkleY, Norm_LAnkleZ, Norm_LAnkleX1, Norm_LAnkleY1, Norm_LAnkleZ1, Norm_LAnkleX2, Norm_LAnkleY2, Norm_LAnkleZ2, \
        Norm_LAnkleX3, Norm_LAnkleY3, Norm_LAnkleZ3, Norm_LAnkleX4, Norm_LAnkleY4, Norm_LAnkleZ4, \
        Norm_LAnkleX5, Norm_LAnkleY5, Norm_LAnkleZ5 \
        = data_NormZero("LAnkleAngles")

    Norm_LFootProX, Norm_LFootProY, Norm_LFootProZ, Norm_LFootProX1, Norm_LFootProY1, Norm_LFootProZ1, Norm_LFootProX2, Norm_LFootProY2, Norm_LFootProZ2, \
        Norm_LFootProX3, Norm_LFootProY3, Norm_LFootProZ3, Norm_LFootProX4, Norm_LFootProY4, Norm_LFootProZ4, \
        Norm_LFootProX5, Norm_LFootProY5, Norm_LFootProZ5 \
        = data_NormZero("LFootProgressAngles")

    Norm_LHeadAnglesX, Norm_LHeadAnglesY, Norm_LHeadAnglesZ, Norm_LHeadAnglesX1, Norm_LHeadAnglesY1, Norm_LHeadAnglesZ1, Norm_LHeadAnglesX2, Norm_LHeadAnglesY2, Norm_LHeadAnglesZ2, \
        Norm_LHeadAnglesX3, Norm_LHeadAnglesY3, Norm_LHeadAnglesZ3, Norm_LHeadAnglesX4, Norm_LHeadAnglesY4, Norm_LHeadAnglesZ4, \
        Norm_LHeadAnglesX5, Norm_LHeadAnglesY5, Norm_LHeadAnglesZ5 \
        = data_NormZero("LHeadAngles")

    Norm_LThoraxAnglesX, Norm_LThoraxAnglesY, Norm_LThoraxAnglesZ, Norm_LThoraxAnglesX1, Norm_LThoraxAnglesY1, Norm_LThoraxAnglesZ1, \
        Norm_LThoraxAnglesX2, Norm_LThoraxAnglesY2, Norm_LThoraxAnglesZ2, Norm_LThoraxAnglesX3, Norm_LThoraxAnglesY3, Norm_LThoraxAnglesZ3, \
        Norm_LThoraxAnglesX4, Norm_LThoraxAnglesY4, Norm_LThoraxAnglesZ4, Norm_LThoraxAnglesX5, Norm_LThoraxAnglesY5, Norm_LThoraxAnglesZ5 \
        = data_NormZero("LThoraxAngles")

    Norm_LNeckAnglesX, Norm_LNeckAnglesY, Norm_LNeckAnglesZ, Norm_LNeckAnglesX1, Norm_LNeckAnglesY1, Norm_LNeckAnglesZ1, \
        Norm_LNeckAnglesX2, Norm_LNeckAnglesY2, Norm_LNeckAnglesZ2, Norm_LNeckAnglesX3, Norm_LNeckAnglesY3, Norm_LNeckAnglesZ3, \
        Norm_LNeckAnglesX4, Norm_LNeckAnglesY4, Norm_LNeckAnglesZ4, Norm_LNeckAnglesX5, Norm_LNeckAnglesY5, Norm_LNeckAnglesZ5 \
        = data_NormZero("LNeckAngles")

    Norm_LSpineAnglesX, Norm_LSpineAnglesY, Norm_LSpineAnglesZ, Norm_LSpineAnglesX1, Norm_LSpineAnglesY1, Norm_LSpineAnglesZ1, \
        Norm_LSpineAnglesX2, Norm_LSpineAnglesY2, Norm_LSpineAnglesZ2, Norm_LSpineAnglesX3, Norm_LSpineAnglesY3, Norm_LSpineAnglesZ3, \
        Norm_LSpineAnglesX4, Norm_LSpineAnglesY4, Norm_LSpineAnglesZ4, Norm_LSpineAnglesX5, Norm_LSpineAnglesY5, Norm_LSpineAnglesZ5 \
        = data_NormZero("LSpineAngles")

    Norm_LShoulderAnglesX, Norm_LShoulderAnglesY, Norm_LShoulderAnglesZ, Norm_LShoulderAnglesX1, Norm_LShoulderAnglesY1, Norm_LShoulderAnglesZ1, \
        Norm_LShoulderAnglesX2, Norm_LShoulderAnglesY2, Norm_LShoulderAnglesZ2, Norm_LShoulderAnglesX3, Norm_LShoulderAnglesY3, Norm_LShoulderAnglesZ3, \
        Norm_LShoulderAnglesX4, Norm_LShoulderAnglesY4, Norm_LShoulderAnglesZ4, Norm_LShoulderAnglesX5, Norm_LShoulderAnglesY5, Norm_LShoulderAnglesZ5 \
        = data_NormZero("LShoulderAngles")

    Norm_LElbowAnglesX, Norm_LElbowAnglesY, Norm_LElbowAnglesZ, Norm_LElbowAnglesX1, Norm_LElbowAnglesY1, Norm_LElbowAnglesZ1, \
        Norm_LElbowAnglesX2, Norm_LElbowAnglesY2, Norm_LElbowAnglesZ2, Norm_LElbowAnglesX3, Norm_LElbowAnglesY3, Norm_LElbowAnglesZ3, \
        Norm_LElbowAnglesX4, Norm_LElbowAnglesY4, Norm_LElbowAnglesZ4, Norm_LElbowAnglesX5, Norm_LElbowAnglesY5, Norm_LElbowAnglesZ5 \
        = data_NormZero("LElbowAngles")

    Norm_LWristAnglesX, Norm_LWristAnglesY, Norm_LWristAnglesZ, Norm_LWristAnglesX1, Norm_LWristAnglesY1, Norm_LWristAnglesZ1, \
        Norm_LWristAnglesX2, Norm_LWristAnglesY2, Norm_LWristAnglesZ2, Norm_LWristAnglesX3, Norm_LWristAnglesY3, Norm_LWristAnglesZ3, \
        Norm_LWristAnglesX4, Norm_LWristAnglesY4, Norm_LWristAnglesZ4, Norm_LWristAnglesX5, Norm_LWristAnglesY5, Norm_LWristAnglesZ5 \
        = data_NormZero("LWristAngles")

    Norm_LHipMX, Norm_LHipMY, Norm_LHipMZ, Norm_LHipMX1, Norm_LHipMY1, Norm_LHipMZ1, \
        Norm_LHipMX2, Norm_LHipMY2, Norm_LHipMZ2, Norm_LHipMX3, Norm_LHipMY3, Norm_LHipMZ3, \
        Norm_LHipMX4, Norm_LHipMY4, Norm_LHipMZ4, Norm_LHipMX5, Norm_LHipMY5, Norm_LHipMZ5 \
        = data_NormZero('LHipMoment')

    Norm_TLHipPX, Norm_TLHipPY, Norm_TLHipPZ, Norm_TLHipPX1, Norm_TLHipPY1, Norm_TLHipPZ1, \
        Norm_TLHipPX2, Norm_TLHipPY2, Norm_TLHipPZ2, Norm_TLHipPX3, Norm_TLHipPY3, Norm_TLHipPZ3, \
        Norm_TLHipPX4, Norm_TLHipPY4, Norm_TLHipPZ4, Norm_TLHipPX5, Norm_TLHipPY5, Norm_TLHipPZ5 \
        = data_NormZero('LHipPower')

    Norm_LKneeMX, Norm_LKneeMY, Norm_LKneeMZ, Norm_LKneeMX1, Norm_LKneeMY1, Norm_LKneeMZ1, \
        Norm_LKneeMX2, Norm_LKneeMY2, Norm_LKneeMZ2, Norm_LKneeMX3, Norm_LKneeMY3, Norm_LKneeMZ3, \
        Norm_LKneeMX4, Norm_LKneeMY4, Norm_LKneeMZ4, Norm_LKneeMX5, Norm_LKneeMY5, Norm_LKneeMZ5 \
        = data_NormZero('LKneeMoment')

    Norm_TLKneePX, Norm_TLKneePY, Norm_TLKneePZ, Norm_TLKneePX1, Norm_TLKneePY1, Norm_TLKneePZ1, \
        Norm_TLKneePX2, Norm_TLKneePY2, Norm_TLKneePZ2, Norm_TLKneePX3, Norm_TLKneePY3, Norm_TLKneePZ3, \
        Norm_TLKneePX4, Norm_TLKneePY4, Norm_TLKneePZ4, Norm_TLKneePX5, Norm_TLKneePY5, Norm_TLKneePZ5 \
        = data_NormZero('LKneePower')

    Norm_LAnkleMX, Norm_LAnkleMY, Norm_LAnkleMZ, Norm_LAnkleMX1, Norm_LAnkleMY1, Norm_LAnkleMZ1, \
        Norm_LAnkleMX2, Norm_LAnkleMY2, Norm_LAnkleMZ2, Norm_LAnkleMX3, Norm_LAnkleMY3, Norm_LAnkleMZ3, \
        Norm_LAnkleMX4, Norm_LAnkleMY4, Norm_LAnkleMZ4, Norm_LAnkleMX5, Norm_LAnkleMY5, Norm_LAnkleMZ5 \
        = data_NormZero('LAnkleMoment')

    Norm_TLAnklePX, Norm_TLAnklePY, Norm_TLAnklePZ, Norm_TLAnklePX1, Norm_TLAnklePY1, Norm_TLAnklePZ1, \
        Norm_TLAnklePX2, Norm_TLAnklePY2, Norm_TLAnklePZ2, Norm_TLAnklePX3, Norm_TLAnklePY3, Norm_TLAnklePZ3, \
        Norm_TLAnklePX4, Norm_TLAnklePY4, Norm_TLAnklePZ4, Norm_TLAnklePX5, Norm_TLAnklePY5, Norm_TLAnklePZ5 \
        = data_NormZero('LAnklePower')

if right_gait_cycle >= 1:
    Norm_RPelvisX, Norm_RPelvisY, Norm_RPelvisZ, Norm_RPelvisX1, Norm_RPelvisY1, Norm_RPelvisZ1, Norm_RPelvisX2, Norm_RPelvisY2, Norm_RPelvisZ2, \
        Norm_RPelvisX3, Norm_RPelvisY3, Norm_RPelvisZ3, Norm_RPelvisX4, Norm_RPelvisY4, Norm_RPelvisZ4, \
        Norm_RPelvisX5, Norm_RPelvisY5, Norm_RPelvisZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RPelvisAngles")

    Norm_RHipX, Norm_RHipY, Norm_RHipZ, Norm_RHipX1, Norm_RHipY1, Norm_RHipZ1, Norm_RHipX2, Norm_RHipY2, Norm_RHipZ2, \
        Norm_RHipX3, Norm_RHipY3, Norm_RHipZ3, Norm_RHipX4, Norm_RHipY4, Norm_RHipZ4, \
        Norm_RHipX5, Norm_RHipY5, Norm_RHipZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RHipAngles")

    Norm_RKneeX, Norm_RKneeY, Norm_RKneeZ, Norm_RKneeX1, Norm_RKneeY1, Norm_RKneeZ1, Norm_RKneeX2, Norm_RKneeY2, Norm_RKneeZ2, \
        Norm_RKneeX3, Norm_RKneeY3, Norm_RKneeZ3, Norm_RKneeX4, Norm_RKneeY4, Norm_RKneeZ4, Norm_RKneeX5, Norm_RKneeY5, Norm_RKneeZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RKneeAngles")

    Norm_RAnkleX, Norm_RAnkleY, Norm_RAnkleZ, Norm_RAnkleX1, Norm_RAnkleY1, Norm_RAnkleZ1, Norm_RAnkleX2, Norm_RAnkleY2, Norm_RAnkleZ2, \
        Norm_RAnkleX3, Norm_RAnkleY3, Norm_RAnkleZ3, Norm_RAnkleX4, Norm_RAnkleY4, Norm_RAnkleZ4, \
        Norm_RAnkleX5, Norm_RAnkleY5, Norm_RAnkleZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RAnkleAngles")

    Norm_RFootProX, Norm_RFootProY, Norm_RFootProZ, Norm_RFootProX1, Norm_RFootProY1, Norm_RFootProZ1, Norm_RFootProX2, Norm_RFootProY2, Norm_RFootProZ2, \
        Norm_RFootProX3, Norm_RFootProY3, Norm_RFootProZ3, Norm_RFootProX4, Norm_RFootProY4, Norm_RFootProZ4, \
        Norm_RFootProX5, Norm_RFootProY5, Norm_RFootProZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RFootProgressAngles")

    Norm_RHeadAnglesX, Norm_RHeadAnglesY, Norm_RHeadAnglesZ, Norm_RHeadAnglesX1, Norm_RHeadAnglesY1, Norm_RHeadAnglesZ1, Norm_RHeadAnglesX2, Norm_RHeadAnglesY2, Norm_RHeadAnglesZ2, \
        Norm_RHeadAnglesX3, Norm_RHeadAnglesY3, Norm_RHeadAnglesZ3, Norm_RHeadAnglesX4, Norm_RHeadAnglesY4, Norm_RHeadAnglesZ4, \
        Norm_RHeadAnglesX5, Norm_RHeadAnglesY5, Norm_RHeadAnglesZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RHeadAngles")

    Norm_RThoraxAnglesX, Norm_RThoraxAnglesY, Norm_RThoraxAnglesZ, Norm_RThoraxAnglesX1, Norm_RThoraxAnglesY1, Norm_RThoraxAnglesZ1, \
        Norm_RThoraxAnglesX2, Norm_RThoraxAnglesY2, Norm_RThoraxAnglesZ2, Norm_RThoraxAnglesX3, Norm_RThoraxAnglesY3, Norm_RThoraxAnglesZ3, \
        Norm_RThoraxAnglesX4, Norm_RThoraxAnglesY4, Norm_RThoraxAnglesZ4, Norm_RThoraxAnglesX5, Norm_RThoraxAnglesY5, Norm_RThoraxAnglesZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RThoraxAngles")

    Norm_RNeckAnglesX, Norm_RNeckAnglesY, Norm_RNeckAnglesZ, Norm_RNeckAnglesX1, Norm_RNeckAnglesY1, Norm_RNeckAnglesZ1, \
        Norm_RNeckAnglesX2, Norm_RNeckAnglesY2, Norm_RNeckAnglesZ2, Norm_RNeckAnglesX3, Norm_RNeckAnglesY3, Norm_RNeckAnglesZ3, \
        Norm_RNeckAnglesX4, Norm_RNeckAnglesY4, Norm_RNeckAnglesZ4, Norm_RNeckAnglesX5, Norm_RNeckAnglesY5, Norm_RNeckAnglesZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RNeckAngles")

    Norm_RSpineAnglesX, Norm_RSpineAnglesY, Norm_RSpineAnglesZ, Norm_RSpineAnglesX1, Norm_RSpineAnglesY1, Norm_RSpineAnglesZ1, \
        Norm_RSpineAnglesX2, Norm_RSpineAnglesY2, Norm_RSpineAnglesZ2, Norm_RSpineAnglesX3, Norm_RSpineAnglesY3, Norm_RSpineAnglesZ3, \
        Norm_RSpineAnglesX4, Norm_RSpineAnglesY4, Norm_RSpineAnglesZ4, Norm_RSpineAnglesX5, Norm_RSpineAnglesY5, Norm_RSpineAnglesZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RSpineAngles")

    Norm_RShoulderAnglesX, Norm_RShoulderAnglesY, Norm_RShoulderAnglesZ, Norm_RShoulderAnglesX1, Norm_RShoulderAnglesY1, Norm_RShoulderAnglesZ1, \
        Norm_RShoulderAnglesX2, Norm_RShoulderAnglesY2, Norm_RShoulderAnglesZ2, Norm_RShoulderAnglesX3, Norm_RShoulderAnglesY3, Norm_RShoulderAnglesZ3, \
        Norm_RShoulderAnglesX4, Norm_RShoulderAnglesY4, Norm_RShoulderAnglesZ4, Norm_RShoulderAnglesX5, Norm_RShoulderAnglesY5, Norm_RShoulderAnglesZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RShoulderAngles")

    Norm_RElbowAnglesX, Norm_RElbowAnglesY, Norm_RElbowAnglesZ, Norm_RElbowAnglesX1, Norm_RElbowAnglesY1, Norm_RElbowAnglesZ1, \
        Norm_RElbowAnglesX2, Norm_RElbowAnglesY2, Norm_RElbowAnglesZ2, Norm_RElbowAnglesX3, Norm_RElbowAnglesY3, Norm_RElbowAnglesZ3, \
        Norm_RElbowAnglesX4, Norm_RElbowAnglesY4, Norm_RElbowAnglesZ4, Norm_RElbowAnglesX5, Norm_RElbowAnglesY5, Norm_RElbowAnglesZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RElbowAngles")

    Norm_RWristAnglesX, Norm_RWristAnglesY, Norm_RWristAnglesZ, Norm_RWristAnglesX1, Norm_RWristAnglesY1, Norm_RWristAnglesZ1, \
        Norm_RWristAnglesX2, Norm_RWristAnglesY2, Norm_RWristAnglesZ2, Norm_RWristAnglesX3, Norm_RWristAnglesY3, Norm_RWristAnglesZ3, \
        Norm_RWristAnglesX4, Norm_RWristAnglesY4, Norm_RWristAnglesZ4, Norm_RWristAnglesX5, Norm_RWristAnglesY5, Norm_RWristAnglesZ5 \
        = data_Norm_Kinematics_Right(RightStrike, right_gait_cycle, "RWristAngles")

    Norm_RHipMX, Norm_RHipMY, Norm_RHipMZ, Norm_RHipMX1, Norm_RHipMY1, Norm_RHipMZ1, \
        Norm_RHipMX2, Norm_RHipMY2, Norm_RHipMZ2, Norm_RHipMX3, Norm_RHipMY3, Norm_RHipMZ3, \
        Norm_RHipMX4, Norm_RHipMY4, Norm_RHipMZ4, Norm_RHipMX5, Norm_RHipMY5, Norm_RHipMZ5 \
        = data_Norm_Kinetics_Right(RightStrike, right_gait_cycle, 'RHipMoment')

    Norm_TRHipPX, Norm_TRHipPY, Norm_TRHipPZ, Norm_TRHipPX1, Norm_TRHipPY1, Norm_TRHipPZ1, \
        Norm_TRHipPX2, Norm_TRHipPY2, Norm_TRHipPZ2, Norm_TRHipPX3, Norm_TRHipPY3, Norm_TRHipPZ3, \
        Norm_TRHipPX4, Norm_TRHipPY4, Norm_TRHipPZ4, Norm_TRHipPX5, Norm_TRHipPY5, Norm_TRHipPZ5 \
        = data_Norm_Kinetics_Right(RightStrike, right_gait_cycle, 'RHipPower')

    Norm_RKneeMX, Norm_RKneeMY, Norm_RKneeMZ, Norm_RKneeMX1, Norm_RKneeMY1, Norm_RKneeMZ1, \
        Norm_RKneeMX2, Norm_RKneeMY2, Norm_RKneeMZ2, Norm_RKneeMX3, Norm_RKneeMY3, Norm_RKneeMZ3, \
        Norm_RKneeMX4, Norm_RKneeMY4, Norm_RKneeMZ4, Norm_RKneeMX5, Norm_RKneeMY5, Norm_RKneeMZ5 \
        = data_Norm_Kinetics_Right(RightStrike, right_gait_cycle, 'RKneeMoment')

    Norm_TRKneePX, Norm_TRKneePY, Norm_TRKneePZ, Norm_TRKneePX1, Norm_TRKneePY1, Norm_TRKneePZ1, \
        Norm_TRKneePX2, Norm_TRKneePY2, Norm_TRKneePZ2, Norm_TRKneePX3, Norm_TRKneePY3, Norm_TRKneePZ3, \
        Norm_TRKneePX4, Norm_TRKneePY4, Norm_TRKneePZ4, Norm_TRKneePX5, Norm_TRKneePY5, Norm_TRKneePZ5 \
        = data_Norm_Kinetics_Right(RightStrike, right_gait_cycle, 'RKneePower')

    Norm_RAnkleMX, Norm_RAnkleMY, Norm_RAnkleMZ, Norm_RAnkleMX1, Norm_RAnkleMY1, Norm_RAnkleMZ1, \
        Norm_RAnkleMX2, Norm_RAnkleMY2, Norm_RAnkleMZ2, Norm_RAnkleMX3, Norm_RAnkleMY3, Norm_RAnkleMZ3, \
        Norm_RAnkleMX4, Norm_RAnkleMY4, Norm_RAnkleMZ4, Norm_RAnkleMX5, Norm_RAnkleMY5, Norm_RAnkleMZ5 \
        = data_Norm_Kinetics_Right(RightStrike, right_gait_cycle, 'RAnkleMoment')

    Norm_TRAnklePX, Norm_TRAnklePY, Norm_TRAnklePZ, Norm_TRAnklePX1, Norm_TRAnklePY1, Norm_TRAnklePZ1, \
        Norm_TRAnklePX2, Norm_TRAnklePY2, Norm_TRAnklePZ2, Norm_TRAnklePX3, Norm_TRAnklePY3, Norm_TRAnklePZ3, \
        Norm_TRAnklePX4, Norm_TRAnklePY4, Norm_TRAnklePZ4, Norm_TRAnklePX5, Norm_TRAnklePY5, Norm_TRAnklePZ5 \
        = data_Norm_Kinetics_Right(RightStrike, right_gait_cycle, 'RAnklePower')

else:
    Norm_RPelvisX, Norm_RPelvisY, Norm_RPelvisZ, Norm_RPelvisX1, Norm_RPelvisY1, Norm_RPelvisZ1, \
        Norm_RPelvisX2, Norm_RPelvisY2, Norm_RPelvisZ2, Norm_RPelvisX3, Norm_RPelvisY3, Norm_RPelvisZ3, \
        Norm_RPelvisX4, Norm_RPelvisY4, Norm_RPelvisZ4, Norm_RPelvisX5, Norm_RPelvisY5, Norm_RPelvisZ5 \
        = data_NormZero("RPelvisAngles")

    Norm_RHipX, Norm_RHipY, Norm_RHipZ, Norm_RHipX1, Norm_RHipY1, Norm_RHipZ1, Norm_RHipX2, Norm_RHipY2, Norm_RHipZ2, \
        Norm_RHipX3, Norm_RHipY3, Norm_RHipZ3, Norm_RHipX4, Norm_RHipY4, Norm_RHipZ4, \
        Norm_RHipX5, Norm_RHipY5, Norm_RHipZ5 \
        = data_NormZero("RHipAngles")

    Norm_RKneeX, Norm_RKneeY, Norm_RKneeZ, Norm_RKneeX1, Norm_RKneeY1, Norm_RKneeZ1, Norm_RKneeX2, Norm_RKneeY2, Norm_RKneeZ2, \
        Norm_RKneeX3, Norm_RKneeY3, Norm_RKneeZ3, Norm_RKneeX4, Norm_RKneeY4, Norm_RKneeZ4, \
        Norm_RKneeX5, Norm_RKneeY5, Norm_RKneeZ5 \
        = data_NormZero("RKneeAngles")

    Norm_RAnkleX, Norm_RAnkleY, Norm_RAnkleZ, Norm_RAnkleX1, Norm_RAnkleY1, Norm_RAnkleZ1, Norm_RAnkleX2, Norm_RAnkleY2, Norm_RAnkleZ2, \
        Norm_RAnkleX3, Norm_RAnkleY3, Norm_RAnkleZ3, Norm_RAnkleX4, Norm_RAnkleY4, Norm_RAnkleZ4, \
        Norm_RAnkleX5, Norm_RAnkleY5, Norm_RAnkleZ5 \
        = data_NormZero("RAnkleAngles")

    Norm_RFootProX, Norm_RFootProY, Norm_RFootProZ, Norm_RFootProX1, Norm_RFootProY1, Norm_RFootProZ1, Norm_RFootProX2, Norm_RFootProY2, Norm_RFootProZ2, \
        Norm_RFootProX3, Norm_RFootProY3, Norm_RFootProZ3, Norm_RFootProX4, Norm_RFootProY4, Norm_RFootProZ4, \
        Norm_RFootProX5, Norm_RFootProY5, Norm_RFootProZ5 \
        = data_NormZero("RFootProgressAngles")

    Norm_RHeadAnglesX, Norm_RHeadAnglesY, Norm_RHeadAnglesZ, Norm_RHeadAnglesX1, Norm_RHeadAnglesY1, Norm_RHeadAnglesZ1, Norm_RHeadAnglesX2, Norm_RHeadAnglesY2, Norm_RHeadAnglesZ2, \
        Norm_RHeadAnglesX3, Norm_RHeadAnglesY3, Norm_RHeadAnglesZ3, Norm_RHeadAnglesX4, Norm_RHeadAnglesY4, Norm_RHeadAnglesZ4, \
        Norm_RHeadAnglesX5, Norm_RHeadAnglesY5, Norm_RHeadAnglesZ5 \
        = data_NormZero("RHeadAngles")

    Norm_RThoraxAnglesX, Norm_RThoraxAnglesY, Norm_RThoraxAnglesZ, Norm_RThoraxAnglesX1, Norm_RThoraxAnglesY1, Norm_RThoraxAnglesZ1, \
        Norm_RThoraxAnglesX2, Norm_RThoraxAnglesY2, Norm_RThoraxAnglesZ2, Norm_RThoraxAnglesX3, Norm_RThoraxAnglesY3, Norm_RThoraxAnglesZ3, \
        Norm_RThoraxAnglesX4, Norm_RThoraxAnglesY4, Norm_RThoraxAnglesZ4, Norm_RThoraxAnglesX5, Norm_RThoraxAnglesY5, Norm_RThoraxAnglesZ5 \
        = data_NormZero("RThoraxAngles")

    Norm_RNeckAnglesX, Norm_RNeckAnglesY, Norm_RNeckAnglesZ, Norm_RNeckAnglesX1, Norm_RNeckAnglesY1, Norm_RNeckAnglesZ1, \
        Norm_RNeckAnglesX2, Norm_RNeckAnglesY2, Norm_RNeckAnglesZ2, Norm_RNeckAnglesX3, Norm_RNeckAnglesY3, Norm_RNeckAnglesZ3, \
        Norm_RNeckAnglesX4, Norm_RNeckAnglesY4, Norm_RNeckAnglesZ4, Norm_RNeckAnglesX5, Norm_RNeckAnglesY5, Norm_RNeckAnglesZ5 \
        = data_NormZero("RNeckAngles")

    Norm_RSpineAnglesX, Norm_RSpineAnglesY, Norm_RSpineAnglesZ, Norm_RSpineAnglesX1, Norm_RSpineAnglesY1, Norm_RSpineAnglesZ1, \
        Norm_RSpineAnglesX2, Norm_RSpineAnglesY2, Norm_RSpineAnglesZ2, Norm_RSpineAnglesX3, Norm_RSpineAnglesY3, Norm_RSpineAnglesZ3, \
        Norm_RSpineAnglesX4, Norm_RSpineAnglesY4, Norm_RSpineAnglesZ4, Norm_RSpineAnglesX5, Norm_RSpineAnglesY5, Norm_RSpineAnglesZ5 \
        = data_NormZero("RSpineAngles")

    Norm_RShoulderAnglesX, Norm_RShoulderAnglesY, Norm_RShoulderAnglesZ, Norm_RShoulderAnglesX1, Norm_RShoulderAnglesY1, Norm_RShoulderAnglesZ1, \
        Norm_RShoulderAnglesX2, Norm_RShoulderAnglesY2, Norm_RShoulderAnglesZ2, Norm_RShoulderAnglesX3, Norm_RShoulderAnglesY3, Norm_RShoulderAnglesZ3, \
        Norm_RShoulderAnglesX4, Norm_RShoulderAnglesY4, Norm_RShoulderAnglesZ4, Norm_RShoulderAnglesX5, Norm_RShoulderAnglesY5, Norm_RShoulderAnglesZ5 \
        = data_NormZero("RShoulderAngles")

    Norm_RElbowAnglesX, Norm_RElbowAnglesY, Norm_RElbowAnglesZ, Norm_RElbowAnglesX1, Norm_RElbowAnglesY1, Norm_RElbowAnglesZ1, \
        Norm_RElbowAnglesX2, Norm_RElbowAnglesY2, Norm_RElbowAnglesZ2, Norm_RElbowAnglesX3, Norm_RElbowAnglesY3, Norm_RElbowAnglesZ3, \
        Norm_RElbowAnglesX4, Norm_RElbowAnglesY4, Norm_RElbowAnglesZ4, Norm_RElbowAnglesX5, Norm_RElbowAnglesY5, Norm_RElbowAnglesZ5 \
        = data_NormZero("RElbowAngles")

    Norm_RWristAnglesX, Norm_RWristAnglesY, Norm_RWristAnglesZ, Norm_RWristAnglesX1, Norm_RWristAnglesY1, Norm_RWristAnglesZ1, \
        Norm_RWristAnglesX2, Norm_RWristAnglesY2, Norm_RWristAnglesZ2, Norm_RWristAnglesX3, Norm_RWristAnglesY3, Norm_RWristAnglesZ3, \
        Norm_RWristAnglesX4, Norm_RWristAnglesY4, Norm_RWristAnglesZ4, Norm_RWristAnglesX5, Norm_RWristAnglesY5, Norm_RWristAnglesZ5 \
        = data_NormZero("RWristAngles")

    Norm_RHipMX, Norm_RHipMY, Norm_RHipMZ = data_NormZero('RHipMoment')
    Norm_TRHipPX, Norm_TRHipPY, Norm_TRHipPZ = data_NormZero('RHipPower')
    Norm_RKneeMX, Norm_RKneeMY, Norm_RKneeMZ = data_NormZero('RKneeMoment')
    Norm_TRKneePX, Norm_TRKneePY, Norm_TRKneePZ = data_NormZero('RKneePower')
    Norm_RAnkleMX, Norm_RAnkleMY, Norm_RAnkleMZ = data_NormZero('RAnkleMoment')
    Norm_TRAnklePX, Norm_TRAnklePY, Norm_TRAnklePZ = data_NormZero('RAnklePower')

LPelvisX, LPelvisY, LPelvisZ = data_PugInGait("LPelvisAngles")
LHipX, LHipY, LHipZ = data_PugInGait("LHipAngles")
LKneeX, LKneeY, LKneeZ = data_PugInGait("LKneeAngles")
LAnkleX, LAnkleY, LAnkleZ = data_PugInGait("LAnkleAngles")
LFootProX, LFootProY, LFootProZ = data_PugInGait("LFootProgressAngles")
LHeadAnglesX, LHeadAnglesY, LHeadAnglesZ = data_PugInGait("LHeadAngles")
LThoraxAnglesX, LThoraxAnglesY, LThoraxAnglesZ = data_PugInGait("LThoraxAngles")
LNeckAnglesX, LNeckAnglesY, LNeckAnglesZ = data_PugInGait("LNeckAngles")
LSpineAnglesX, LSpineAnglesY, LSpineAnglesZ = data_PugInGait("LSpineAngles")
LShoulderAnglesX, LShoulderAnglesY, LShoulderAnglesZ = data_PugInGait("LShoulderAngles")
LElbowAnglesX, LElbowAnglesY, LElbowAnglesZ = data_PugInGait("LElbowAngles")
LWristAnglesX, LWristAnglesY, LWristAnglesZ = data_PugInGait("LWristAngles")

LHipMXD, LHipMYD, LHipMZD = data_PlugInGait_moments("LHipMoment")
LHipPZ = data_PlugInGait_power("LHipPower")
LKneeMXD, LKneeMYD, LKneeMZD = data_PlugInGait_moments("LKneeMoment")
LKneePZ = data_PlugInGait_power("LKneePower")
LAnkMXD, LAnkMYD, LAnkMZD = data_PlugInGait_moments("LAnkleMoment")
LAnkPZ = data_PlugInGait_power("LAnklePower")

RPelvisX, RPelvisY, RPelvisZ = data_PugInGait("RPelvisAngles")
RHipX, RHipY, RHipZ = data_PugInGait("RHipAngles")
RKneeX, RKneeY, RKneeZ = data_PugInGait("RKneeAngles")
RAnkleX, RAnkleY, RAnkleZ = data_PugInGait("RAnkleAngles")
RFootProX, RFootProY, RFootProZ = data_PugInGait("RFootProgressAngles")
RHeadAnglesX, RHeadAnglesY, RHeadAnglesZ = data_PugInGait("RHeadAngles")
RThoraxAnglesX, RThoraxAnglesY, RThoraxAnglesZ = data_PugInGait("RThoraxAngles")
RNeckAnglesX, RNeckAnglesY, RNeckAnglesZ = data_PugInGait("RNeckAngles")
RSpineAnglesX, RSpineAnglesY, RSpineAnglesZ = data_PugInGait("RSpineAngles")
RShoulderAnglesX, RShoulderAnglesY, RShoulderAnglesZ = data_PugInGait("RShoulderAngles")
RElbowAnglesX, RElbowAnglesY, RElbowAnglesZ = data_PugInGait("RElbowAngles")
RWristAnglesX, RWristAnglesY, RWristAnglesZ = data_PugInGait("RWristAngles")

RHipMXD, RHipMYD, RHipMZD = data_PlugInGait_moments("RHipMoment")
RHipPZ = data_PlugInGait_power("RHipPower")
RKneeMXD, RKneeMYD, RKneeMZD = data_PlugInGait_moments("RKneeMoment")
RKneePZ = data_PlugInGait_power("RKneePower")
RAnkMXD, RAnkMYD, RAnkMZD = data_PlugInGait_moments("RAnkleMoment")
RAnkPZ = data_PlugInGait_power("RAnklePower")

# Create excel Worksheet and apply data

workbook = xlsxwriter.Workbook(TrialName + ".xlsx", {'in_memory': False})  # creating excel files

worksheet1 = createworksheet('Subject_Info', 0, 13, 25)
worksheet2 = createworksheet('Norm_Kinematics', 0, 73, 25)
worksheet3 = createworksheet('Norm_Kinetics', 0, 44, 25)
worksheet4 = createworksheet('Norm_Kinematics_Graphs', 0, 26, 10)
worksheet5 = createworksheet('Norm_Kinetics_Graphs', 0, 26, 10)
worksheet6 = createworksheet('Kinematics', 0, 73, 25)
worksheet7 = createworksheet('Kinetics', 0, 44, 25)
worksheet8 = createworksheet('Cycle_1_Kinem', 0, 73, 25)
worksheet9 = createworksheet('Cycle_2_Kinem', 0, 73, 25)
worksheet10 = createworksheet('Cycle_3_Kinem', 0, 73, 25)
worksheet11 = createworksheet('Cycle_4_Kinem', 0, 73, 25)
worksheet12 = createworksheet('Cycle_5_Kinem', 0, 73, 25)
worksheet13 = createworksheet('Cycle_1_Kinet', 0, 73, 25)
worksheet14 = createworksheet('Cycle_2_Kinet', 0, 73, 25)
worksheet15 = createworksheet('Cycle_3_Kinet', 0, 73, 25)
worksheet16 = createworksheet('Cycle_4_Kinet', 0, 73, 25)
worksheet17 = createworksheet('Cycle_5_Kinet', 0, 73, 25)

normal = workbook.add_format({'font_name': 'Calibri'})
bold = workbook.add_format({'bold': True, 'font_name': 'Calibri'})
boldposition = workbook.add_format({'bold': True, 'font_name': 'Calibri'})
boldposition.set_align('center')
boldposition.set_align('vcenter')
boldleft = workbook.add_format({'bold': True, 'font_name': 'Calibri'})
boldleft.set_font_color('#CC0C0C')
boldleft.set_align('center')
boldleft.set_align('vcenter')
boldright = workbook.add_format({'bold': True, 'font_name': 'Calibri'})
boldright.set_font_color('#053C5E')
boldright.set_align('center')
boldright.set_align('vcenter')
setbackground(worksheet1)

# Write Subject Information to worksheet 1
worksheet1.write('B3', 'Trial Information', boldposition)
worksheet1.write('B4', 'Trial Name: ', bold)
worksheet1.write('B5', '', bold)
worksheet1.write('C3', '', bold)
worksheet1.write('C4', TrialName1, normal)
worksheet1.write('C5', '', bold)
worksheet1.write('F2', 'Links to Data Sheets ', boldposition)
worksheet1.write_url('F3', 'internal:Norm_Kinematics!A1', string='Normalized Kinematics')
worksheet1.write_url('F4', 'internal:Norm_Kinetics!A1', string='Normalized Kinetics')
worksheet1.write_url('F5', 'internal:Norm_Kinematics_Graphs!A1',
                     string='Normalized Kinematics Graphs')
worksheet1.write_url('F6', 'internal:Norm_Kinetics_Graphs!A1', string='Normalized Kinetics Graphs')
worksheet1.write_url('F7', 'internal:Kinematics!A1', string='Kinematics')
worksheet1.write_url('F8', 'internal:Kinetics!A1', string='Kinetics')
worksheet1.write_url('F9', 'internal:Cycle_1_Kinem!A1', string='Gait Cycle 1 Kinematics')
worksheet1.write_url('F10', 'internal:Cycle_2_Kinem!A1', string='Gait Cycle 2 Kinematics')
worksheet1.write_url('F11', 'internal:Cycle_3_Kinem!A1', string='Gait Cycle 3 Kinematics')
worksheet1.write_url('F12', 'internal:Cycle_4_Kinem!A1', string='Gait Cycle 4 Kinematics')
worksheet1.write_url('F13', 'internal:Cycle_5_Kinem!A1', string='Gait Cycle 5 Kinematics')
worksheet1.write_url('F14', 'internal:Cycle_1_Kinet!A1', string='Gait Cycle 1 Kinetics')
worksheet1.write_url('F15', 'internal:Cycle_2_Kinet!A1', string='Gait Cycle 2 Kinetics')
worksheet1.write_url('F16', 'internal:Cycle_3_Kinet!A1', string='Gait Cycle 3 Kinetics')
worksheet1.write_url('F17', 'internal:Cycle_4_Kinet!A1', string='Gait Cycle 4 Kinetics')
worksheet1.write_url('F18', 'internal:Cycle_5_Kinet!A1', string='Gait Cycle 5 Kinetics')

worksheet1.write('B6', 'Subject Paramaters', boldposition)
worksheet1.write('C6', '', bold)
worksheet1.write('B7', 'Subject Name', bold)
worksheet1.write('C7', SubjectName, normal)

worksheet1.write('B11', 'Context ', boldposition)
worksheet1.write('C11', 'Left', boldleft)
worksheet1.write('D11', 'Right', boldright)

worksheet1.write('B20', 'Analysis ', boldposition)
worksheet1.write('C20', 'Left', boldleft)
worksheet1.write('D20', 'Right', boldright)
worksheet1.write('E20', 'Left_1', boldleft)
worksheet1.write('F20', 'Right_1', boldright)
worksheet1.write('G20', 'Left_2', boldleft)
worksheet1.write('H20', 'Right_2', boldright)
worksheet1.write('I20', 'Left_3', boldleft)
worksheet1.write('J20', 'Right_3', boldright)
worksheet1.write('K20', 'Left_4', boldleft)
worksheet1.write('L20', 'Right_4', boldright)
worksheet1.write('M20', 'Left_5', boldleft)
worksheet1.write('N20', 'Right_5', boldright)

worksheet1.write('B21', 'Gait Cycle Count:', bold)
worksheet1.write('C21', left_gait_cycle, normal)
worksheet1.write('D21', right_gait_cycle, normal)

subjparam('Bodymass(kg): ', 'Bodymass', '', worksheet1, 'B8', 'C8', 'D12')
subjparam('Height (mm): ', 'Height', '', worksheet1, 'B9', 'C9', 'D12')
subjparam('', '', '', worksheet1, 'B10', 'C10', 'D10')

subjparam('Shoulder Offset (mm): ', 'LeftShoulderOffset',
          'RightShoulderOffset', worksheet1, 'B12', 'C12', 'D12')
subjparam('Elbow Width (mm): ', 'LeftElbowWidth',
          'RightElbowWidth', worksheet1, 'B13', 'C13', 'D13')
subjparam('Wrist Width (mm): ', 'LeftWristWidth',
          'RightWristWidth', worksheet1, 'B14', 'C14', 'D14')
subjparam('Hand Thickness (mm): ', 'LeftHandThickness',
          'RightHandThickness', worksheet1, 'B15', 'C15', 'D15')
subjparam('Leg Length (mm): ', 'LeftLegLength', 'RightLegLength', worksheet1, 'B16', 'C16', 'D16')
subjparam('Knee Width (mm): ', 'LeftKneeWidth', 'RightKneeWidth', worksheet1, 'B17', 'C17', 'D17')
subjparam('Ankle Width (mm): ', 'LeftAnkleWidth',
          'RightAnkleWidth', worksheet1, 'B18', 'C18', 'D18')

analysisout('Cadence (steps/min): ', 'LeftCadence', 'RightCadence', worksheet1, 'B22', 'C22', 'D22')
analysisout('Cadence (steps/min): ', 'LeftCadence_1', 'RightCadence_1', worksheet1, 'B22', 'E22', 'F22')
analysisout('Cadence (steps/min): ', 'LeftCadence_2', 'RightCadence_2', worksheet1, 'B22', 'G22', 'H22')
analysisout('Cadence (steps/min): ', 'LeftCadence_3', 'RightCadence_3', worksheet1, 'B22', 'I22', 'J22')
analysisout('Cadence (steps/min): ', 'LeftCadence_4', 'RightCadence_4', worksheet1, 'B22', 'K22', 'L22')
analysisout('Cadence (steps/min): ', 'LeftCadence_5', 'RightCadence_5', worksheet1, 'B22', 'M22', 'N22')

analysisout('Walking Speed (m/s): ', 'LeftWalkingSpeed',
            'RightWalkingSpeed', worksheet1, 'B23', 'C23', 'D23')
analysisout('Walking Speed (m/s): ', 'LeftWalkingSpeed_1',
            'RightWalkingSpeed_1', worksheet1, 'B23', 'E23', 'F23')
analysisout('Walking Speed (m/s): ', 'LeftWalkingSpeed_2',
            'RightWalkingSpeed_2', worksheet1, 'B23', 'G23', 'H23')
analysisout('Walking Speed (m/s): ', 'LeftWalkingSpeed_3',
            'RightWalkingSpeed_3', worksheet1, 'B23', 'I23', 'J23')
analysisout('Walking Speed (m/s): ', 'LeftWalkingSpeed_4',
            'RightWalkingSpeed_4', worksheet1, 'B23', 'K23', 'L23')
analysisout('Walking Speed (m/s): ', 'LeftWalkingSpeed_5',
            'RightWalkingSpeed_5', worksheet1, 'B23', 'M23', 'N23')

analysisout('Stride Time (s): ', 'LeftStrideTime',
            'RightStrideTime', worksheet1, 'B24', 'C24', 'D24')
analysisout('Stride Time (s): ', 'LeftStrideTime_1',
            'RightStrideTime_1', worksheet1, 'B24', 'E24', 'F24')
analysisout('Stride Time (s): ', 'LeftStrideTime_2',
            'RightStrideTime_2', worksheet1, 'B24', 'G24', 'H24')
analysisout('Stride Time (s): ', 'LeftStrideTime_3',
            'RightStrideTime_3', worksheet1, 'B24', 'I24', 'J24')
analysisout('Stride Time (s): ', 'LeftStrideTime_4',
            'RightStrideTime_4', worksheet1, 'B24', 'K24', 'L24')
analysisout('Stride Time (s): ', 'LeftStrideTime_5',
            'RightStrideTime_5', worksheet1, 'B24', 'M24', 'N24')

analysisout('Step Time (s): ', 'LeftStepTime', 'RightStepTime', worksheet1, 'B25', 'C25', 'D25')
analysisout('Step Time (s): ', 'LeftStepTime_1', 'RightStepTime_1', worksheet1, 'B25', 'E25', 'F25')
analysisout('Step Time (s): ', 'LeftStepTime_2', 'RightStepTime_2', worksheet1, 'B25', 'G25', 'H25')
analysisout('Step Time (s): ', 'LeftStepTime_3', 'RightStepTime_3', worksheet1, 'B25', 'I25', 'J25')
analysisout('Step Time (s): ', 'LeftStepTime_4', 'RightStepTime_4', worksheet1, 'B25', 'K25', 'L25')
analysisout('Step Time (s): ', 'LeftStepTime_5', 'RightStepTime_5', worksheet1, 'B25', 'M25', 'N25')

analysisout('Opposite Foot Off (%): ', 'LeftOppositeFootOff', 'RightOppositeFootOff', worksheet1, 'B26', 'C26',
            'D26')
analysisout('Opposite Foot Off (%): ', 'LeftOppositeFootOff_1', 'RightOppositeFootOff_1', worksheet1, 'B26', 'E26',
            'F26')
analysisout('Opposite Foot Off (%): ', 'LeftOppositeFootOff_2', 'RightOppositeFootOff_2', worksheet1, 'B26', 'G26',
            'H26')
analysisout('Opposite Foot Off (%): ', 'LeftOppositeFootOff_3', 'RightOppositeFootOff_3', worksheet1, 'B26', 'I26',
            'J26')
analysisout('Opposite Foot Off (%): ', 'LeftOppositeFootOff_4', 'RightOppositeFootOff_4', worksheet1, 'B26', 'K26',
            'L26')
analysisout('Opposite Foot Off (%): ', 'LeftOppositeFootOff_5', 'RightOppositeFootOff_5', worksheet1, 'B26', 'M26',
            'N26')

analysisout('Opposite Foot Contact (%): ', 'LeftOppositeFootContact', 'RightOppositeFootContact', worksheet1, 'B27',
            'C27', 'D27')
analysisout('Opposite Foot Contact (%): ', 'LeftOppositeFootContact_1', 'RightOppositeFootContact_1', worksheet1, 'B27',
            'E27', 'F27')
analysisout('Opposite Foot Contact (%): ', 'LeftOppositeFootContact_2', 'RightOppositeFootContact_2', worksheet1, 'B27',
            'G27', 'H27')
analysisout('Opposite Foot Contact (%): ', 'LeftOppositeFootContact_3', 'RightOppositeFootContact_3', worksheet1, 'B27',
            'I27', 'J27')
analysisout('Opposite Foot Contact (%): ', 'LeftOppositeFootContact_4', 'RightOppositeFootContact_4', worksheet1, 'B27',
            'K27', 'L27')
analysisout('Opposite Foot Contact (%): ', 'LeftOppositeFootContact_5', 'RightOppositeFootContact_5', worksheet1, 'B27',
            'M27', 'N27')


analysisout('Foot Off (%): ', 'LeftFootOff', 'RightFootOff', worksheet1, 'B28', 'C28', 'D28')
analysisout('Foot Off (%): ', 'LeftFootOff_1', 'RightFootOff_1', worksheet1, 'B28', 'E28', 'F28')
analysisout('Foot Off (%): ', 'LeftFootOff_2', 'RightFootOff_2', worksheet1, 'B28', 'G28', 'H28')
analysisout('Foot Off (%): ', 'LeftFootOff_3', 'RightFootOff_3', worksheet1, 'B28', 'I28', 'J28')
analysisout('Foot Off (%): ', 'LeftFootOff_4', 'RightFootOff_4', worksheet1, 'B28', 'K28', 'L28')
analysisout('Foot Off (%): ', 'LeftFootOff_5', 'RightFootOff_5', worksheet1, 'B28', 'M28', 'N28')

analysisout('Double Support (s): ', 'LeftDoubleSupport',
            'RightDoubleSupport', worksheet1, 'B29', 'C29', 'D29')
analysisout('Double Support (s): ', 'LeftDoubleSupport_1',
            'RightDoubleSupport_1', worksheet1, 'B29', 'E29', 'F29')
analysisout('Double Support (s): ', 'LeftDoubleSupport_2',
            'RightDoubleSupport_2', worksheet1, 'B29', 'G29', 'H29')
analysisout('Double Support (s): ', 'LeftDoubleSupport_3',
            'RightDoubleSupport_3', worksheet1, 'B29', 'I29', 'J29')
analysisout('Double Support (s): ', 'LeftDoubleSupport_4',
            'RightDoubleSupport_4', worksheet1, 'B29', 'K29', 'L29')
analysisout('Double Support (s): ', 'LeftDoubleSupport_5',
            'RightDoubleSupport_5', worksheet1, 'B29', 'M29', 'N29')

analysisout('Stride Length (m): ', 'LeftStrideLength',
            'RightStrideLength', worksheet1, 'B30', 'C30', 'D30')
analysisout('Stride Length (m): ', 'LeftStrideLength_1',
            'RightStrideLength_1', worksheet1, 'B30', 'E30', 'F30')
analysisout('Stride Length (m): ', 'LeftStrideLength_2',
            'RightStrideLength_2', worksheet1, 'B30', 'G30', 'H30')
analysisout('Stride Length (m): ', 'LeftStrideLength_3',
            'RightStrideLength_3', worksheet1, 'B30', 'I30', 'J30')
analysisout('Stride Length (m): ', 'LeftStrideLength_4',
            'RightStrideLength_4', worksheet1, 'B30', 'K30', 'L30')
analysisout('Stride Length (m): ', 'LeftStrideLength_5',
            'RightStrideLength_5', worksheet1, 'B30', 'M30', 'N30')

analysisout('Step Length (m): ', 'LeftStepLength',
            'RightStepLength', worksheet1, 'B31', 'C31', 'D31')
analysisout('Step Length (m): ', 'LeftStepLength_1',
            'RightStepLength_1', worksheet1, 'B31', 'E31', 'F31')
analysisout('Step Length (m): ', 'LeftStepLength_2',
            'RightStepLength_2', worksheet1, 'B31', 'G31', 'H31')
analysisout('Step Length (m): ', 'LeftStepLength_3',
            'RightStepLength_3', worksheet1, 'B31', 'I31', 'J31')
analysisout('Step Length (m): ', 'LeftStepLength_4',
            'RightStepLength_4', worksheet1, 'B31', 'K31', 'L31')
analysisout('Step Length (m): ', 'LeftStepLength_5',
            'RightStepLength_5', worksheet1, 'B31', 'M31', 'N31')

analysisout('Step Width (m): ', 'LeftStepWidth',
            'RightStepWidth', worksheet1, 'B32', 'C32', 'D32')
analysisout('Step Width (m): ', 'LeftStepWidth_1',
            'RightStepWidth_1', worksheet1, 'B32', 'E32', 'F32')
analysisout('Step Width (m): ', 'LeftStepWidth_2',
            'RightStepWidth_2', worksheet1, 'B32', 'G32', 'H32')
analysisout('Step Width (m): ', 'LeftStepWidth_3',
            'RightStepWidth_3', worksheet1, 'B32', 'I32', 'J32')
analysisout('Step Width (m): ', 'LeftStepWidth_4',
            'RightStepWidth_4', worksheet1, 'B32', 'K32', 'L32')
analysisout('Step Width (m): ', 'LeftStepWidth_5',
            'RightStepWidth_5', worksheet1, 'B32', 'M32', 'N32')

analysisout('Limp Index: ', 'LeftLimp Index', 'RightLimp Index', worksheet1, 'B33', 'C33', 'D33')
analysisout('GDI Index: ', 'LeftGDI', 'RightGDI', worksheet1, 'B34', 'C34', 'D34')

worksheet1.set_tab_color('#6495EC')

worksheet_headings_kinem(worksheet2)
worksheet_headings_kine(worksheet3)
worksheet_headings_kinem(worksheet6)
worksheet_headings_kine(worksheet7)
worksheet_headings_kinem(worksheet8)
worksheet_headings_kinem(worksheet9)
worksheet_headings_kinem(worksheet10)
worksheet_headings_kinem(worksheet11)
worksheet_headings_kinem(worksheet12)
worksheet_headings_kine(worksheet13)
worksheet_headings_kine(worksheet14)
worksheet_headings_kine(worksheet15)
worksheet_headings_kine(worksheet16)
worksheet_headings_kine(worksheet17)

worksheet2.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet3.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet6.write('A1', 'Frame', boldposition)
worksheet7.write('A1', 'Frame', boldposition)
worksheet8.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet9.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet10.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet11.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet12.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet13.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet14.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet15.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet16.write('A1', 'Percentage of Gait Cycle', boldposition)
worksheet17.write('A1', 'Percentage of Gait Cycle', boldposition)

if left_gait_cycle or right_gait_cycle >= 1:
    writedataexcel(data_NormKinematics(), worksheet2, "#6495EC")
    writedataexcel(data_NormKinetics(), worksheet3, "#6495EC")
    writedataexcel(data_NormKinematics1(), worksheet8, "#6495EC")
    writedataexcel(data_NormKinematics2(), worksheet9, "#6495EC")
    writedataexcel(data_NormKinematics3(), worksheet10, "#6495EC")
    writedataexcel(data_NormKinematics4(), worksheet11, "#6495EC")
    writedataexcel(data_NormKinematics5(), worksheet12, "#6495EC")
    writedataexcel(data_NormKinetics1(), worksheet13, "#6495EC")
    writedataexcel(data_NormKinetics2(), worksheet14, "#6495EC")
    writedataexcel(data_NormKinetics3(), worksheet15, "#6495EC")
    writedataexcel(data_NormKinetics4(), worksheet16, "#6495EC")
    writedataexcel(data_NormKinetics5(), worksheet17, "#6495EC")

else:
    comment = 'No Gait Cycles present to Normalise Data'
    worksheet2.set_tab_color('#FF3300')
    worksheet2.write_comment('A2', comment, dict(visible=True))
    worksheet4.set_tab_color('#FF3300')
    worksheet3.set_tab_color('#FF3300')
    worksheet3.write_comment('A2', comment, dict(visible=True))
    worksheet5.set_tab_color('#FF3300')
    print('Red Tabs in Excel Worksheet contains no data due to: No Gait Cycles')

writedataexcel(data_Kinematics(), worksheet6, "#6495EC")
writedataexcel(data_Kinetics(), worksheet7, "#6495EC")

# Create Kinematics Graphs
# Left and Right Pelvis X
Chart1Kinematics = createnormchart('=Norm_Kinematics!$A$2:$A$101', '=Norm_Kinematics!$B$2:$B$101',
                                   '=Norm_Kinematics!$E$2:$E$101',
                                   'Pelvic tilt', 'Angle', 0, 100, 10)

# Left and Right Pelvis Y
Chart2Kinematics = createnormchart('=Norm_Kinematics!$A$2:$A$101', '=Norm_Kinematics!$C$2:$C$101',
                                   '=Norm_Kinematics!$F$2:$F$101',
                                   'Pelvic obliquity', 'Angle', -30, 30, 10)

# Left and Right Pelvis Z
Chart3Kinematics = createnormchart('=Norm_Kinematics!$A$2:$A$101', '=Norm_Kinematics!$D$2:$D$101',
                                   '=Norm_Kinematics!$G$2:$G$101',
                                   'Pelvic rotation', 'Angle', -30, 30, 10)

# Left and Right Hip X
Chart4Kinematics = createnormchart('=Norm_Kinematics!$A$2:$A$101', '=Norm_Kinematics!$H$2:$H$101',
                                   '=Norm_Kinematics!$K$2:$K$101', 'Hip flexion', 'Angle', 0, 100, 10)

# Left and Right Hip Y
Chart5Kinematics = createnormchart('=Norm_Kinematics!$A$2:$A$101', '=Norm_Kinematics!$I$2:$I$101',
                                   '=Norm_Kinematics!$L$2:$L$101',
                                   'Hip adduction', 'Angle', -30, 30, 10)

# Left and Right Hip Z
Chart6Kinematics = createnormchart('=Norm_Kinematics!$A$2:$A$101', '=Norm_Kinematics!$J$2:$J$101',
                                   '=Norm_Kinematics!$M$2:$M$101',
                                   'Hip rotation', 'Angle', -30, 30, 10)

# Left and Right Knee X
Chart7Kinematics = createnormchart('=Norm_Kinematics!$A$2:$A$101', '=Norm_Kinematics!$N$2:$N$101',
                                   '=Norm_Kinematics!$Q$2:$Q$101',
                                   'Knee flexion', 'Angle', -15, 75, 10)

# Left and Right Knee Y
Chart8Kinematics = createnormchart('=Norm_Kinematics!$A$2:$A$101', '=Norm_Kinematics!$O$2:$O$101',
                                   '=Norm_Kinematics!$R$2:$R$101',
                                   'Knee adduction', 'Angle', -30, 30, 10)

# Left and Right Knee Z
Chart9Kinematics = createnormchart('=Norm_Kinematics!$A$2:$A$101', '=Norm_Kinematics!$P$2:$P$101',
                                   '=Norm_Kinematics!$S$2:$S$101',
                                   'Knee rotation', 'Angle', -30, 30, 10)

# Create Kinetics Graphs
# Left and Right Hip X
Chart1Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$B$2:$B$101',
                                 '=Norm_Kinetics!$F$2:$F$101',
                                 'Hip extensor moment', 'Nm/kg', -2.0, 3.0, 1.0)

# Left and Right Hip Y
Chart2Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$C$2:$C$101',
                                 '=Norm_Kinetics!$G$2:$G$101',
                                 'Hip abductor moment', 'Nm/kg', -1.0, 2.0, 1.0)

# Left and Right Hip Z
Chart3Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$D$2:$D$101',
                                 '=Norm_Kinetics!$H$2:$H$101',
                                 'Hip rotation moment', 'Nm/kg', -0.5, 0.5, 1.0)

# Left and Right Knee X
Chart4Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$J$2:$J$101',
                                 '=Norm_Kinetics!$N$2:$N$101',
                                 'Knee extensor moment', 'Nm/kg', -1, 1, 1.0)

# Left and Right Knee Y
Chart5Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$K$2:$K$101',
                                 '=Norm_Kinetics!$O$2:$O$101',
                                 'Knee abductor moment', 'Nm/kg', -1, 1, 1.0)

# Left and Right Knee Z
Chart6Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$L$2:$L$101',
                                 '=Norm_Kinetics!$P$2:$P$101',
                                 'Knee rotation moment', 'Nm/kg', -0.5, 0.5, 1.0)

# Left and Right Ankle X
Chart7Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$R$2:$R$101',
                                 '=Norm_Kinetics!$V$2:$V$101',
                                 'Plantarflexor moment', 'Nm/kg', -1, 3, 1.0)

# Left and Right Ankle Y
Chart8Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$S$2:$S$101',
                                 '=Norm_Kinetics!$W$2:$W$101',
                                 'Ankle evertor moment', 'Nm/kg', -0.5, 0.5, 1.0)

# Left and Right Ankle Z
Chart9Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$T$2:$T$101',
                                 '=Norm_Kinetics!$X$2:$X$101',
                                 'Ankle rotation moment', 'Nm/kg', -0.5, 0.5, 1.0)

# Left and Right Total Hip Power
Chart10Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$E$2:$E$101',
                                  '=Norm_Kinetics!$I$2:$I$101',
                                  'Total hip power', 'W', -3, 3, 1.0)

# Left and Right Total Knee Power
Chart11Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$M$2:$M$101',
                                  '=Norm_Kinetics!$Q$2:$Q$101',
                                  'Total knee power', 'W', -3, 3, 1.0)

# Left and Right Total Ankle Power
Chart12Kinetics = createnormchart('=Norm_Kinetics!$A$2:$A$101', '=Norm_Kinetics!$U$2:$U$101',
                                  '=Norm_Kinetics!$Y$2:$Y$101',
                                  'Total ankle power', 'W', -2, 5, 1.0)
# Insert the chart into the worksheet (with an offset).
worksheet4.insert_chart('A2', Chart1Kinematics, {'x_offset': 25, 'y_offset': 10})
worksheet4.insert_chart('I2', Chart2Kinematics, {'x_offset': 25, 'y_offset': 10})
worksheet4.insert_chart('Q2', Chart3Kinematics, {'x_offset': 25, 'y_offset': 10})
worksheet4.insert_chart('A18', Chart4Kinematics, {'x_offset': 25, 'y_offset': 10})
worksheet4.insert_chart('I18', Chart5Kinematics, {'x_offset': 25, 'y_offset': 10})
worksheet4.insert_chart('Q18', Chart6Kinematics, {'x_offset': 25, 'y_offset': 10})
worksheet4.insert_chart('A34', Chart7Kinematics, {'x_offset': 25, 'y_offset': 10})
worksheet4.insert_chart('I34', Chart8Kinematics, {'x_offset': 25, 'y_offset': 10})
worksheet4.insert_chart('Q34', Chart9Kinematics, {'x_offset': 25, 'y_offset': 10})

worksheet5.insert_chart('A2', Chart1Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('I2', Chart2Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('Q2', Chart3Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('A18', Chart4Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('I18', Chart5Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('Q18', Chart6Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('A34', Chart7Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('I34', Chart8Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('Q34', Chart9Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('A50', Chart10Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('I50', Chart11Kinetics, {'x_offset': 25, 'y_offset': 10})
worksheet5.insert_chart('Q50', Chart12Kinetics, {'x_offset': 25, 'y_offset': 10})

workbook.close()

