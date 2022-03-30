(this.webpackJsonphandpose = this.webpackJsonphandpose || []).push([
  [0],
  {
    247: function (e, t, n) {
      e.exports = n(274);
    },
    252: function (e, t, n) {},
    258: function (e, t) {},
    259: function (e, t) {},
    267: function (e, t) {},
    270: function (e, t) {},
    271: function (e, t) {},
    272: function (e, t, n) {},
    274: function (e, t, n) {
      "use strict";
      n.r(t);
      var r = n(64),
        a = n.n(r),
        o = n(226),
        c = n.n(o),
        i = (n(252), n(5)),
        u = n.n(i),
        s = n(13),
        l = (n(273), n(246)),
        f = n(245),
        d = n.n(f),
        h = (n(272), n(8)),
        p = function (e, t) {
          console.log(e),
            e.forEach(function (e) {
              var n = Object(h.a)(e.bbox, 4),
                r = n[0],
                a = n[1],
                o = n[2],
                c = n[3],
                i = e.class,
                u = Math.floor(16777215 * Math.random()).toString(16);
              (t.strokeStyle = "#" + u),
                (t.font = "18px Arial"),
                t.beginPath(),
                (t.fillStyle = "#" + u),
                t.fillText(i, r, a),
                t.rect(r, a, o, c),
                t.stroke();
            });
        };
      var g = function () {
        var e = Object(r.useRef)(null),
          t = Object(r.useRef)(null),
          n = (function () {
            var e = Object(s.a)(
              u.a.mark(function e() {
                var t;
                return u.a.wrap(function (e) {
                  for (;;)
                    switch ((e.prev = e.next)) {
                      case 0:
                        return (e.next = 2), l.a();
                      case 2:
                        (t = e.sent),
                          console.log("Handpose model loaded."),
                          setInterval(function () {
                            o(t);
                          }, 10);
                      case 5:
                      case "end":
                        return e.stop();
                    }
                }, e);
              })
            );
            return function () {
              return e.apply(this, arguments);
            };
          })(),
          o = (function () {
            var n = Object(s.a)(
              u.a.mark(function n(r) {
                var a, o, c, i, s;
                return u.a.wrap(function (n) {
                  for (;;)
                    switch ((n.prev = n.next)) {
                      case 0:
                        if (
                          "undefined" === typeof e.current ||
                          null === e.current ||
                          4 !== e.current.video.readyState
                        ) {
                          n.next = 13;
                          break;
                        }
                        return (
                          (a = e.current.video),
                          (o = e.current.video.videoWidth),
                          (c = e.current.video.videoHeight),
                          (e.current.video.width = o),
                          (e.current.video.height = c),
                          (t.current.width = o),
                          (t.current.height = c),
                          (n.next = 10),
                          r.detect(a)
                        );
                      case 10:
                        (i = n.sent), (s = t.current.getContext("2d")), p(i, s);
                      case 13:
                      case "end":
                        return n.stop();
                    }
                }, n);
              })
            );
            return function (e) {
              return n.apply(this, arguments);
            };
          })();
        return (
          Object(r.useEffect)(function () {
            n();
          }, []),
          a.a.createElement(
            "div",
            { className: "App" },
            a.a.createElement(
              "header",
              { className: "App-header" },
              a.a.createElement(d.a, {
                ref: e,
                muted: !0,
                style: {
                  position: "absolute",
                  marginLeft: "auto",
                  marginRight: "auto",
                  left: 0,
                  right: 0,
                  textAlign: "center",
                  zindex: 9,
                  width: 640,
                  height: 480,
                },
              }),
              a.a.createElement("canvas", {
                ref: t,
                style: {
                  position: "absolute",
                  marginLeft: "auto",
                  marginRight: "auto",
                  left: 0,
                  right: 0,
                  textAlign: "center",
                  zindex: 8,
                  width: 640,
                  height: 480,
                },
              })
            )
          )
        );
      };
      c.a.render(
        a.a.createElement(a.a.StrictMode, null, a.a.createElement(g, null)),
        document.getElementById("root")
      );
    },
  },
  [[247, 1, 2]],
]);
//# sourceMappingURL=main.7b62e473.chunk.js.map
