import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 350
    height: 450
    title: "Swipe_View"

    SwipeView {
        id: swipeView
        anchors.fill: parent

        Page {
            id: redPage

            Rectangle {
                color: "red"
                anchors.fill: parent

                Text {
                    text: "Red Page"
                    color: "white"
                    font.pixelSize: 24
                    anchors.centerIn: parent
                }
            }
        }

        Page {
            id: yellowPage

            Rectangle {
                color: "yellow"
                anchors.fill: parent

                Text {
                    text: "Yellow Page"
                    color: "black"
                    font.pixelSize: 24
                    anchors.centerIn: parent
                }
            }
        }

        Page {
            id: greenPage

            Rectangle {
                color: "green"
                anchors.fill: parent

                Text {
                    text: "Green Page"
                    color: "white"
                    font.pixelSize: 24
                    anchors.centerIn: parent
                }
            }
        }
    }

    PageIndicator {
        id: pageIndicator
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 20

        count: swipeView.count
        currentIndex: swipeView.currentIndex
    }
}
