#ifndef HTTP_H
#define HTTP_H

#include <QObject>
#include <QNetworkAccessManager>
#include <QNetworkReply>
#include <QJsonObject>
#include <QJsonArray>
#include <QJsonDocument>
#include "spaceobject.h"

class HTTP : public QObject
{
    Q_OBJECT
private:
    QNetworkAccessManager* manager = nullptr;
    QString received_json;
    QList<SpaceObject> spaceObjects;

public:
    explicit HTTP(QObject *parent = nullptr);
    void send_request(QString url);

    QString get_received_json();
    QList<SpaceObject>& get_space_objects();
    void set_space_objects(QList<SpaceObject> list);
public slots:
    void get_response(QNetworkReply* reply);

signals:
    void SpaceObjectListUpdated(QList<SpaceObject> list);
};

#endif // HTTP_H
