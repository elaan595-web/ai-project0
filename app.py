from flask import Flask, render_template, request

app = Flask(__name__)


# 🟢 الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("index.html")


# 🟡 خطوة 2
@app.route("/step2", methods=["POST"])
def step2():
    step1 = request.form.get("text", "")
    return render_template("step2.html", step1=step1)


# 🔵 النتيجة النهائية
@app.route("/result", methods=["POST"])
def result():

    # 📥 البيانات (تصحيح مهم جدًا)
    step1 = request.form.get("step1", "").lower()
    step2 = request.form.get("step2", "").lower()
    step3 = request.form.get("step3", "").lower()

    text = step1 + " " + step2 + " " + step3
    words = len(text.split())

    ai_score = 0
    feedback = []

    # =========================
    # 🤖 كلمات أكاديمية
    # =========================
    academic_words = [
        "effective", "algorithm", "accuracy", "model",
        "prediction", "variance", "generalization",
        "decision", "trees", "features", "data",
        "classification", "performance", "method",
        "approach", "analysis", "evaluation",
        "optimization", "training", "testing"
    ]

    for w in academic_words:
        if w in text:
            ai_score += 8

    # =========================
    # 📏 طول النص
    # =========================
    if words > 120:
        ai_score += 15

    if words < 40:
        feedback.append("write more details")

    # =========================
    # 🔁 تنظيم AI
    # =========================
    if "for example" in text and "because" in text:
        ai_score += 15

    # =========================
    # 🧠 عبارات AI
    # =========================
    ai_phrases = [
        "this approach",
        "this method",
        "is useful because",
        "it is important to note",
        "in conclusion"
    ]

    for phrase in ai_phrases:
        if phrase in text:
            ai_score += 10

    # =========================
    # 📊 تقنية
    # =========================
    tech_words = ["model", "data", "accuracy", "feature", "tree"]
    tech_count = sum(1 for w in tech_words if w in text)

    if tech_count >= 4:
        ai_score += 10

    # =========================
    # 🎯 تحديد النتيجة
    # =========================
    if ai_score >= 40:
        level = "🔴 AI-like Writing Detected"
        coach_message = "This writing is highly structured and similar to AI-generated academic style."

    elif ai_score >= 20:
        level = "🟡 Mixed Writing Style"
        coach_message = "This looks partly structured. Try writing more naturally."

    else:
        level = "🟢 Human-like Writing"
        coach_message = "This looks like natural student writing."

    return render_template(
        "result.html",
        score=ai_score,
        level=level,
        coach_message=coach_message,
        feedback=feedback
    )


if __name__ == "__main__":
    app.run(debug=True)