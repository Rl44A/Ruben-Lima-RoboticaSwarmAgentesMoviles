function mocap_data = robotat_get_pose(tcp_obj, agents_ids)
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here
    timeout_count = 0;
    read(tcp_obj);

    if((min(agents_ids) > 0) && (max(agents_ids) <= 100))
        write(tcp_obj, uint8(jsonencode(round(agents_ids))))
        while((tcp_obj.BytesAvailable == 0) && (timeout_count < 80000))
            timeout_count = timeout_count + 1;
        end
        if(timeout_count == 80000)
            disp('ERROR: Could not receive data from server.');
            return;
        else
            mocap_data = jsondecode(char(read(tcp_obj)));
            mocap_data = reshape(mocap_data, [numel(agents_ids), 7]);
        end
    else
        disp('ERROR: Invalid ID(s).');
    end
end