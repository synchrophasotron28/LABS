#include "http.h"

HTTP::HTTP(QObject *parent) : QObject(parent)
{
    manager = new QNetworkAccessManager();
    connect(manager, &QNetworkAccessManager::finished, this, &HTTP::get_response);
}

void HTTP::send_request(QString url)
{
    manager->get(QNetworkRequest(QUrl(url)));
}

QString HTTP::get_received_json()
{
    return received_json;
}

QList<SpaceObject> &HTTP::get_space_objects()
{
    return spaceObjects;
}

void HTTP::get_response(QNetworkReply *reply)
{
    QJsonDocument jsonDocument(QJsonDocument::fromJson(reply->readAll()));
    QJsonObject jsonObject = jsonDocument.object();
    spaceObjects.clear();

    foreach (QString key, jsonObject.keys())
    {
        SpaceObject spaceobject;

        spaceobject.name = key;
        spaceobject.x = jsonObject[key].toObject()["x"].toDouble();
        spaceobject.y = jsonObject[key].toObject()["y"].toDouble();
        spaceobject.z = jsonObject[key].toObject()["z"].toDouble();
        spaceobject.theta = jsonObject[key].toObject()["theta"].toDouble();
        spaceobject.h_p = jsonObject[key].toObject()["h_p"].toDouble();
        spaceobject.h_a = jsonObject[key].toObject()["h_a"].toDouble();
        spaceobject.r = jsonObject[key].toObject()["r"].toDouble();
        spaceobject.p = jsonObject[key].toObject()["p"].toDouble();
        spaceobject.OMEGA = jsonObject[key].toObject()["OMEGA"].toDouble();
        spaceobject.omega = jsonObject[key].toObject()["omega"].toDouble();
        spaceobject.e = jsonObject[key].toObject()["e"].toDouble();
        spaceobject.U = jsonObject[key].toObject()["U"].toDouble();
        spaceobject.tau = jsonObject[key].toObject()["tau"].toDouble();
        spaceobject.m = jsonObject[key].toObject()["m"].toDouble();
        spaceobject.i = jsonObject[key].toObject()["i"].toDouble();

        spaceObjects << spaceobject;
    }

    qDebug() << "spaceObjects";
}

