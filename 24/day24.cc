#include <complex>
#include <fstream>
#include <iostream>
#include <regex>
#include <vector>

using namespace std;

template <typename T>
ostream& operator<<(ostream& output, vector<T> const& values) {
    for (auto const& value : values) {
        output << value << endl;
    }
    return output;
}

vector<string> split(const string& line, const regex& sep) {
    sregex_token_iterator iter(line.begin(), line.end(), sep, -1);
    return {iter, sregex_token_iterator()};
}

int main() {
    // const double start_area = 7, end_area = 27;
    const double start_area = 200000000000000, end_area = 400000000000000;
    fstream file("input.txt", ios::in);
    string line;

    vector<complex<double>> pos;
    vector<complex<double>> vels;

    while (getline(file, line)) {
        vector<string> spli = split(line, regex("[\\s|,|@]+"));
        if (line.empty()) {
            continue;
        }
        pos.emplace_back(stod(spli[0]), stod(spli[1]));
        vels.emplace_back(stod(spli[3]), stod(spli[4]));
    }
    cout << "Read done\n";
    file.close();

    size_t n_colls = 0;
    for (size_t i = 0; i < pos.size(); ++i) {
        // TODO: Check if stone passes through area.
        double k1 = vels[i].imag() / vels[i].real();
        double m1 = pos[i].imag() - k1 * pos[i].real();
        for (size_t j = i + 1; j < pos.size(); ++j) {
            double k2 = vels[j].imag() / vels[j].real();
            double m2 = pos[j].imag() - k2 * pos[j].real();

            if (k1 == k2) {
                continue;
            }

            double x_inter = (m2 - m1) / (k1 - k2);
            double y_inter = k1 * x_inter + m1;
            double t1 = (x_inter - pos[i].real()) / vels[i].real();
            double t2 = (x_inter - pos[j].real()) / vels[j].real();

            if (x_inter >= start_area && x_inter <= end_area && y_inter >= start_area && y_inter <= end_area && t1 > 0 && t2 > 0) {
                n_colls++;
            } 
        }
    }

    cout << "res: " << n_colls << endl;
}
