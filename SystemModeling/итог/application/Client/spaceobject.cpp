#include "spaceobject.h"

SpaceObject::SpaceObject(QObject *parent)
{

}

SpaceObject::SpaceObject(QString name,double x, double y, double z,
                         double theta,
                         double h_p, double h_a,
                         double r, double p,
                         double OMEGA, double omega,
                         double e, double U,
                         double tau, double m,
                         double i) :name(name),
    x(x), y(y), z(z),
    theta(theta),
    h_p(h_p), h_a(h_a),
    r(r), p(p),
    OMEGA(OMEGA),omega(omega),
    e(e),U(U),tau(tau),m(m),i(i)
{

}
