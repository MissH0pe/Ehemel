from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QLabel, QLineEdit, QCheckBox
from PySide6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        raceCount = 8
        races = ["Deep Sea Folk", "Druss", "Frost Elves", "Goblins", "Naga", "Sky Dwarves", "Swamp Orcs", "Yupir"]

        self.setWindowTitle("Ehemel Character Sheet")

        mainLayout = QGridLayout()

        cdLayout = QGridLayout()
        nameLayout = QGridLayout()
        raceLayout = QGridLayout()
        raceGrid1Layout = QGridLayout()
        raceGrid2Layout = QGridLayout()

        statsLayout = QGridLayout()
        pStatsLayout = QGridLayout()
        dStatsLayout = QGridLayout()


        titleLabel = QLabel("Ehemel Character Sheet")
        fontTitleLabel = titleLabel.font()
        fontTitleLabel.setPointSize(30)
        titleLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        mainLayout.addWidget(titleLabel, 0, 0)


        nameLabel = QLabel("Name")
        nameBox = QLineEdit()
        nameLayout.addWidget(nameLabel, 0, 0)
        nameLayout.addWidget(nameBox, 0, 1)


        racesLabel = QLabel("Races or Subraces")
        raceLayout.addWidget(racesLabel, 0, 0)


        races1Labels = []
        races1CheckBoxes = []

        for k in range(int(raceCount / 6)):
            races1Labels.append(QLabel(races[k]))
            races1CheckBoxes.append(QCheckBox())
            raceGrid1Layout.addWidget(races1Labels[k], k, 0)
            raceGrid1Layout.addWidget(races1CheckBoxes[k], k, 1)

            races1Labels.append(QLabel(races[k + 1]))
            races1CheckBoxes.append(QCheckBox())
            raceGrid1Layout.addWidget(races1Labels[k + 1], k, 2)
            raceGrid1Layout.addWidget(races1CheckBoxes[k + 1], k, 3)

            races1Labels.append(QLabel(races[k + 2]))
            races1CheckBoxes.append(QCheckBox())
            raceGrid1Layout.addWidget(races1Labels[k + 2], k, 4)
            raceGrid1Layout.addWidget(races1CheckBoxes[k + 2], k, 5)

            races1Labels.append(QLabel(races[k + 3]))
            races1CheckBoxes.append(QCheckBox())
            raceGrid1Layout.addWidget(races1Labels[k + 3], k, 6)
            raceGrid1Layout.addWidget(races1CheckBoxes[k + 3], k, 7)

            races1Labels.append(QLabel(races[k + 4]))
            races1CheckBoxes.append(QCheckBox())
            raceGrid1Layout.addWidget(races1Labels[k + 4], k, 8)
            raceGrid1Layout.addWidget(races1CheckBoxes[k + 4], k, 9)

            races1Labels.append(QLabel(races[k + 5]))
            races1CheckBoxes.append(QCheckBox())
            raceGrid1Layout.addWidget(races1Labels[k + 5], k, 10)
            raceGrid1Layout.addWidget(races1CheckBoxes[k + 5], k, 11)


        races2CheckBoxes = []
        races2Labels = []

        for k in range(raceCount % 6):
            races2Labels.append(QLabel(races[(6 * int(raceCount / 6)) + k]))
            races2CheckBoxes.append(QCheckBox())
            raceGrid2Layout.addWidget(races2Labels[k], 0, (k * 2))
            raceGrid2Layout.addWidget(races2CheckBoxes[k], 0, (k * 2) + 1)


        statsLabel = QLabel("Main Statistics")
        fontStatsLabel = statsLabel.font()
        fontStatsLabel.setPointSize(30)
        statsLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        statsLayout.addWidget(statsLabel, 0, 0)


        strengthLabel = QLabel("Strength")
        strengthBox = QLineEdit()
        pStatsLayout.addWidget(strengthLabel, 0, 0)
        pStatsLayout.addWidget(strengthBox, 0, 1)

        dexterityLabel = QLabel("Dexterity")
        dexterityBox = QLineEdit()
        pStatsLayout.addWidget(dexterityLabel, 1, 0)
        pStatsLayout.addWidget(dexterityBox, 1, 1)

        constitutionLabel = QLabel("Constitution")
        constitutionBox = QLineEdit()
        pStatsLayout.addWidget(constitutionLabel, 2, 0)
        pStatsLayout.addWidget(constitutionBox, 2, 1)

        vitalityLabel = QLabel("Vitality")
        vitalityBox = QLineEdit()
        pStatsLayout.addWidget(vitalityLabel, 3, 0)
        pStatsLayout.addWidget(vitalityBox, 3, 1)


        charismaLabel = QLabel("Charisma")
        charismaBox = QLineEdit()
        pStatsLayout.addWidget(charismaLabel, 0, 2)
        pStatsLayout.addWidget(charismaBox, 0, 3)

        manipulationLabel = QLabel("Manipulation")
        manipulationBox = QLineEdit()
        pStatsLayout.addWidget(manipulationLabel, 1, 2)
        pStatsLayout.addWidget(manipulationBox, 1, 3)

        composureLabel = QLabel("Composure")
        composureBox = QLineEdit()
        pStatsLayout.addWidget(composureLabel, 2, 2)
        pStatsLayout.addWidget(composureBox, 2, 3)

        prideLabel = QLabel("Pride")
        prideBox = QLineEdit()
        pStatsLayout.addWidget(prideLabel, 3, 2)
        pStatsLayout.addWidget(prideBox, 3, 3)


        intellectLabel = QLabel("Intellect")
        intellectBox = QLineEdit()
        pStatsLayout.addWidget(intellectLabel, 0, 4)
        pStatsLayout.addWidget(intellectBox, 0, 5)

        witsLabel = QLabel("Wits")
        witsBox = QLineEdit()
        pStatsLayout.addWidget(witsLabel, 1, 4)
        pStatsLayout.addWidget(witsBox, 1, 5)

        resolveLabel = QLabel("Resolve")
        resolveBox = QLineEdit()
        pStatsLayout.addWidget(resolveLabel, 2, 4)
        pStatsLayout.addWidget(resolveBox, 2, 5)

        magicLabel = QLabel("Magic")
        magicBox = QLineEdit()
        pStatsLayout.addWidget(magicLabel, 3, 4)
        pStatsLayout.addWidget(magicBox, 3, 5)


        chealthLabel = QLabel("Current Health")
        chealthBox = QLineEdit()
        mhealthLabel = QLabel("Max Health")
        mhealthBox = QLineEdit()
        dStatsLayout.addWidget(chealthLabel, 0, 0)
        dStatsLayout.addWidget(chealthBox, 0, 1)
        dStatsLayout.addWidget(mhealthLabel, 0, 2)
        dStatsLayout.addWidget(mhealthBox, 0, 3)

        ccourageLabel = QLabel("Current Courage")
        ccourageBox = QLineEdit()
        mcourageLabel = QLabel("Max Courage")
        mcourageBox = QLineEdit()
        dStatsLayout.addWidget(ccourageLabel, 0, 4)
        dStatsLayout.addWidget(ccourageBox, 0, 5)
        dStatsLayout.addWidget(mcourageLabel, 0, 6)
        dStatsLayout.addWidget(mcourageBox, 0, 7)

        cmanaLabel = QLabel("Current Mana")
        cmanaBox = QLineEdit()
        mmanaLabel = QLabel("Max Mana")
        mmanaBox = QLineEdit()
        dStatsLayout.addWidget(cmanaLabel, 0, 8)
        dStatsLayout.addWidget(cmanaBox, 0, 9)
        dStatsLayout.addWidget(mmanaLabel, 0, 10)
        dStatsLayout.addWidget(mmanaBox, 0, 11)

        raceLayout.addLayout(raceGrid1Layout, 1, 0)
        raceLayout.addLayout(raceGrid2Layout, 2, 0)

        cdLayout.addLayout(nameLayout, 0, 0)
        cdLayout.addLayout(raceLayout, 0, 1)

        statsLayout.addWidget(statsLabel, 0, 0)
        statsLayout.addLayout(pStatsLayout, 1, 0)
        statsLayout.addLayout(dStatsLayout, 2, 0)

        mainLayout.addLayout(cdLayout, 1, 0)
        mainLayout.addLayout(statsLayout, 2, 0)

        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
